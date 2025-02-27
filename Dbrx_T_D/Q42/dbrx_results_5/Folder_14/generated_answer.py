def prime_factors(numbers_list):
    prime_factors = set()
    for num in numbers_list[16:17]:
        for i in range(2, num + 1):
            while num % i == 0:
                prime_factors.add(i)
                num //= i
    return prime_factors