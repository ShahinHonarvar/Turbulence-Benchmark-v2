import sympy 

def all_left_right_truncatable_prime(t):

    def is_truncatable(n):
        while len(n) > 2:
            n = str(n)[1:-1]
            if not sympy.isprime(int(n)):
                return False
        return sympy.isprime(int(n))
    x = t[55]
    for i in range(2, x + 1):
        if sympy.isprime(i):
            if i > 9 and '0' not in str(i) or is_truncatable(i):
                n = int(i)
                while True:
                    n_str = str(n)
                    if n <= 1:
                        break
                    if '0' not in n_str and n % 10 != 0:
                        n1 = int(n_str[1:])
                        n2 = int(n_str[:-1])
                        if not sympy.isprime(n1) or not sympy.isprime(n2):
                            if len(n_str) == 2:
                                primes.append(n)
                        else:
                            n = min(n1, n2)
                    else:
                        break
    return sorted(list(set(primes)))