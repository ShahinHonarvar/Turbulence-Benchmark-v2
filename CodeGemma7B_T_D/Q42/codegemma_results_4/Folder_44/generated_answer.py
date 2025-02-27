def prime_factors(num_list):
    prime_factors = set()
    num = num_list[828]
    while num % 2 == 0:
        prime_factors.add(2)
        num //= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            prime_factors.add(i)
            num //= i
    if num > 1:
        prime_factors.add(num)
    return prime_factors