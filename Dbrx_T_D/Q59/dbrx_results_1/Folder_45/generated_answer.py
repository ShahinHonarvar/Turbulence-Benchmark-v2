from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[61]
    left_truncatable_primes = []
    for num in range(1, x):
        string_num = str(num)
        if '0' in string_num:
            continue
        is_left_truncatable_prime = True
        for i in range(1, len(string_num)):
            if not isprime(int(string_num[i:])):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)