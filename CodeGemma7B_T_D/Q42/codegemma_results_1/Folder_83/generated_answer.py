from collections import defaultdict

def prime_factors(li):
    li = li[:96]
    factorDictionary = defaultdict(set)
    for number in li:
        for factor in range(2, int(number ** 0.5) + 1):
            while number % factor == 0:
                factorDictionary[number].add(factor)
                number = number / factor
    for key in factorDictionary:
        if key == li[95]:
            return factorDictionary[key]