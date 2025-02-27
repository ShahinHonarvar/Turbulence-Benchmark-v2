def prime_factors(numbers):
    prime_factors = set()
    for num in numbers[20:21]:
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_factors.add(i)
        if num > 1:
            prime_factors.add(num)
    return prime_factors