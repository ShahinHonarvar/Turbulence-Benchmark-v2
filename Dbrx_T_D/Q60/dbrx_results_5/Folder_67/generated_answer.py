from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[71]
    truncatable_primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            is_truncatable = True
            while num > 10 and is_truncatable:
                num = int(str(num)[1:]) if num % 10 != 0 else int(str(num)[:-1])
                if not isprime(num):
                    is_truncatable = False
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(set(truncatable_primes), reverse=True)