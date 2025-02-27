def prime_factors(num_list):
    factors = set()
    num = num_list[68]
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num != 1:
        factors.add(num)
    return factors