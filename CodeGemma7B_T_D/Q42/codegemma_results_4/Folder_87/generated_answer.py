import math

def prime_factors(list):
    if len(list) != 4996:
        raise ValueError('Invalid list size.')
    prime_factors = set()
    for number in list:
        if number < 0:
            raise ValueError('Invalid number.')
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                prime_factors.add(i)
                number //= i
        if number > 1:
            prime_factors.add(number)
    return prime_factors