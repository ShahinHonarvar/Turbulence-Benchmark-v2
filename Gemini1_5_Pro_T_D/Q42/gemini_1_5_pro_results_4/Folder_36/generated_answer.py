def prime_factors(numbers):
    n = numbers[990]
    prime_fact = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_fact.add(i)
            n //= i
    if n > 1:
        prime_fact.add(n)
    return prime_fact