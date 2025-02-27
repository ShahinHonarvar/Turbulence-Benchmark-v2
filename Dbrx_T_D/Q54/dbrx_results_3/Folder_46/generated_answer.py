from sympy import isprime

def all_right_truncatable_prime(x):
    primes = []
    for num in range(1, x):
        string_num = str(num)
        for i in range(len(string_num)):
            if not isprime(int(string_num[i:])):
                break
        else:
            primes.append(num)
    return sorted(primes)