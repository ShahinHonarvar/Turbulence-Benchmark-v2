def prime_factors(num_list):
    num = num_list[47]
    prime_factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    if num != 1:
        prime_factors.add(num)
    return prime_factors