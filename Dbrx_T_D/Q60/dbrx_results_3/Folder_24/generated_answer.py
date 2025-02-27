from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    left_right_truncatable_primes = []
    x = numbers_tuple[65]
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            is_left_right_truncatable = True
            while num > 10 and is_left_right_truncatable:
                num = int(str(num)[1:]) if num < 100 else int(str(num)[:-1])
                if not isprime(num) or '0' in str(num):
                    is_left_right_truncatable = False
            if is_left_right_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(list(set(left_right_truncatable_primes)), reverse=True)