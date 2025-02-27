def prime_factors(num_list):
    if len(num_list) < 10:
        raise ValueError('Input list must have at least 20 elements')
    prime_factors = set()
    n = num_list[19]
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.add(i)
    if n > 1:
        prime_factors.add(n)
    return prime_factors