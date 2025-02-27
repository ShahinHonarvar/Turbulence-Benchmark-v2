from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[91]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            is_left_right_truncatable = True
            while num > 10 and is_left_right_truncatable:
                num = int(str(num)[1:]) if num % 10 != 0 else 0
                if not isprime(num):
                    is_left_right_truncatable = False
            if is_left_right_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)