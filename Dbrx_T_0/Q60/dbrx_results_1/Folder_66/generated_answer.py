from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[25]
    ltrunc_primes = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        is_ltrunc_prime = True
        while num > 9:
            num = int(str(num)[1:]) if num < 100 else int(str(num)[:-1])
            if not isprime(num):
                is_ltrunc_prime = False
                break
        if is_ltrunc_prime:
            ltrunc_primes.append(num)
    return sorted(ltrunc_primes, reverse=True)