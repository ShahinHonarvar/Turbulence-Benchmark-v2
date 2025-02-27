import math

def prime_factors(integer_list):
    prime_factors_set = set()
    number = integer_list[69]
    while number % 2 == 0:
        prime_factors_set.add(2)
        number /= 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors_set.add(i)
            number /= i
    if number > 2:
        prime_factors_set.add(number)
    return prime_factors_set