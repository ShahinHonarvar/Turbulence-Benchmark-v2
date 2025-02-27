def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[:86]:
        for i in range(2, num + 1):
            if num % i == 0:
                prime_factors.add(i)
        if len(prime_factors) > 1:
            prime_factors.remove(1)
    return prime_factors