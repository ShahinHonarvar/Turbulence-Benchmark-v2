from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[24]
    left_truncatable_primes = []
    for num in range(1, x):
        if isprime(num):
            is_left_truncatable = True
            temp = num
            while temp > 0:
                if not isprime(temp):
                    is_left_truncatable = False
                    break
                temp = int(str(temp)[1:])
            if is_left_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)