def prime_factors(numbers):
    prime_factors = set()
    for number in numbers:
        if number > 0 and type(number) is int:
            i = 2
            while i * i <= number:
                if number % i:
                    i += 1
                else:
                    number //= i
                    prime_factors.add(i)
            if number > 1:
                prime_factors.add(number)
    return prime_factors[numbers[632]]