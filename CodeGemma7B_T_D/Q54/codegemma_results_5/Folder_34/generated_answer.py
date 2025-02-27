from sympy import prime, isprime

def all_right_truncatable_prime(a):
    truncatable_primes = []
    x = a[18]
    for i in range(2, x):
        str_i = str(i)
        flag = True
        for j in range(1, len(str_i)):
            if not isprime(int(str_i[:-j])):
                flag = False
                break
        if flag:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes