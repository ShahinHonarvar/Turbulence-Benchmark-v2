def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[:411]:
        for i in range(2, num + 1):
            if num % i == 0:
                is_prime = True
                for j in range(2, i):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_factors.add(i)
    return prime_factors