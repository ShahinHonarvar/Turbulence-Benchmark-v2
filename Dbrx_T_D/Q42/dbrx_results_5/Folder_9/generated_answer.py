def prime_factors(num_list):
    prime_factors = set()
    for num in num_list:
        if num % 2 == 0:
            prime_factors.add(2)
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                prime_factors.add(i)
    return prime_factors