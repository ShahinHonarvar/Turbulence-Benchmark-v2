def prime_factors(numbers):
    prime_factors_746 = set()
    for num in numbers:
        while num % 2 == 0:
            prime_factors_746.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                prime_factors_746.add(i)
                num //= i
        if num > 2:
            prime_factors_746.add(num)
    return prime_factors_746[numbers.index(746)]