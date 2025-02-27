def prime_factors(num_list):
    num = num_list[702]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            num //= i
            factors.add(i)
        else:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors