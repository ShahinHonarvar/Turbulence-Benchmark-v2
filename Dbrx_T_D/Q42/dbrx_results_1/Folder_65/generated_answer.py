def prime_factors(numbers):
    prime_factors_set = set()
    for num in numbers[35:]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i:
                continue
            while num % i == 0:
                prime_factors_set.add(i)
                num //= i
            break
        if num > 1:
            prime_factors_set.add(num)
    return prime_factors_set