def prime_factors(numbers):
    prime_factors_46 = set()
    if len(numbers) >= 46:
        number = numbers[45]
        i = 2
        while i <= number:
            if number % i:
                i += 1
            else:
                number //= i
                prime_factors_46.add(i)
        if number > 1:
            prime_factors_46.add(number)
    return prime_factors_46