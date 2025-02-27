import sympy

def all_right_truncatable_prime(numbers: tuple) -> list:
    if len(numbers) < 98 or not all((isinstance(n, int) and n > 0 for n in numbers)):
        raise ValueError('Input tuple should contain at least 98 positive integers')
    x = numbers[98]
    right_truncatable_primes = []
    for num in range(1, x):
        if sympy.isprime(num):
            is_right_truncatable = True
            temp_num = num
            while temp_num > 9:
                temp_num = temp_num // 10
                if not sympy.isprime(temp_num):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)