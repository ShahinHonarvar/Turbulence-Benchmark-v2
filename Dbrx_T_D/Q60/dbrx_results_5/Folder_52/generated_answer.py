from sympy import isprime

def all_left_right_truncatable_prime(n):
    lr_primes = []
    for i in range(1, n + 1):
        if isprime(i) and '0' not in str(i):
            flag = True
            for j in range(len(str(i))):
                if not isprime(int(str(i)[j:])) or not isprime(int(str(i)[:-j])):
                    flag = False
                    break
            if flag:
                lr_primes.append(i)
    return sorted(lr_primes, reverse=True)