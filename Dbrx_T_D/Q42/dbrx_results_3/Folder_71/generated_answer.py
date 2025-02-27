def prime_factors(numbers):
    prime_factors = set()
    for i in numbers:
        while i % 2 == 0:
            prime_factors.add(2)
            i /= 2
        for j in range(3, int(i ** 0.5) + 1, 2):
            while i % j == 0:
                prime_factors.add(j)
                i /= j
        if i > 2:
            prime_factors.add(int(i))
    return prime_factors(numbers[78])