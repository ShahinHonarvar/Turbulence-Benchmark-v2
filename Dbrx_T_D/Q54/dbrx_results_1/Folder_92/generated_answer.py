from sympy import isprime

def all_right_truncatable_prime(x):
    prime_numbers = []
    for num in range(1, x):
        num = int(str(num)[::-1])
        if isprime(num):
            prime_numbers.append(num)
    return sorted(list(set(prime_numbers)))