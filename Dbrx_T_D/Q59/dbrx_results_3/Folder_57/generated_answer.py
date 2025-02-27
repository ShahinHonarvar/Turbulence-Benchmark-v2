from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[54]
    ltrunc_primes = []
    for num in range(1, x):
        num_str = str(num)
        if int(num_str[0]) == 0:
            continue
        is_ltrunc_prime = all((isprime(int(num_str[i:])) for i in range(1, len(num_str))))
        if is_ltrunc_prime:
            ltrunc_primes.append(num)
    return sorted(ltrunc_primes, reverse=True)