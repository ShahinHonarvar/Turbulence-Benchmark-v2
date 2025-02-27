def prime_factors(numbers):
    index = 68
    prime_factors = set()
    while index < len(numbers):
        num = numbers[index]
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_factors.add(i)
        if num > 1:
            prime_factors.add(num)
        index += 1
    return prime_factors