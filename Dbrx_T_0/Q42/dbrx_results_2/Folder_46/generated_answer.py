def prime_factors(numbers):
    prime_factors = set()
    for num in numbers:
        if num > 453:
            break
        if num == 2:
            prime_factors.add(2)
            continue
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                prime_factors.add(i)
                break
        if num > 2 and num % 2 == 0:
            prime_factors.add(2)
    return prime_factors