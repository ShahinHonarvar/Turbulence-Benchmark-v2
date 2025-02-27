from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[88]
    left_truncatable_primes = []
    for num in range(1, x):
        if isprime(num):
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not isprime(int(str_num[i:])):
                    break
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)