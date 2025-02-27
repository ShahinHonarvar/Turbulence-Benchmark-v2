def prime_factors(x):
    prime_set = set()
    for num in x:
        for i in range(2, num):
            if num % i == 0:
                prime_set.add(i)
    return prime_set