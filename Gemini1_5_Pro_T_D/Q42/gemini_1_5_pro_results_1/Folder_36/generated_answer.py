def prime_factors(numbers):
    n = numbers[990]
    prime_fact = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_fact.add(i)
    if n > 1:
        prime_fact.add(n)
    return prime_fact