from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 20:
        return []
    x = numbers[20]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_right_truncatable = True
        while str_num:
            if not isprime(int(str_num)):
                is_right_truncatable = False
                break
            str_num = str_num[:-1]
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)