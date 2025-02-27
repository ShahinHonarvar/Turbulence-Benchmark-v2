from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    left_truncatable_primes = []
    for num in range(1, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])):
                break
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)