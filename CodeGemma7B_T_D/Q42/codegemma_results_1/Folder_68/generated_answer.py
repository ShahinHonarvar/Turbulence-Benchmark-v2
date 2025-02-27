def prime_factors(num_list):
    prime_factors = set()
    num = num_list[3]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors.add(i)
            num = num // i
    return prime_factors