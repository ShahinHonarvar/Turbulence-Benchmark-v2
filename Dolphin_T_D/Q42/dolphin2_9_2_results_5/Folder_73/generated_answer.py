def prime_factors(numbers):
    prime_factors_set = set()
    index = 41
    if index < len(numbers):
        num = numbers[index]
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                prime_factors_set.add(i)
        if num > 1:
            prime_factors_set.add(num)
    return prime_factors_set