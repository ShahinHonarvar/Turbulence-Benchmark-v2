def prime_factors(num_list):
    if 94 < len(num_list):
        n = num_list[94]
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    else:
        return 'Index out of range'