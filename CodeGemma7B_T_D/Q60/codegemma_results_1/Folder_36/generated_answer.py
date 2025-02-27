from sympy import isprime

def all_left_right_truncatable_prime(x):
    results = []
    for num in range(2, x + 1):
        if not '0' in str(num):
            prime = isprime(num)
            while prime and num > 10:
                num = int(str(num)[1:])
                prime = isprime(num)
            if prime and num in range(2, 10 ** 2):
                results.append(num)
    return sorted(results)