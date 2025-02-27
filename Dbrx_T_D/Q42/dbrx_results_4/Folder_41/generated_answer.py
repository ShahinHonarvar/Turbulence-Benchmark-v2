def prime_factors(numbers):
    prime_factors = set()
    for number in numbers[:85]:
        while number % 2 == 0:
            prime_factors.add(2)
            number = number / 2
        i = 3
        while i * i <= number:
            if number % i:
                i += 2
            else:
                prime_factors.add(i)
                number = number / i
        if number > 2:
            prime_factors.add(int(number))
    return prime_factors