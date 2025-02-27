def prime_factors(numbers):
    return set(prime_factor(27, numbers))

def prime_factor(number, numbers):
    if number in numbers:
        factors = {number}
        index = numbers.index(number)
        for i in range(index + 3, len(numbers), 2):
            if numbers[i] == number + 3:
                number += 3
                factors.add(number)
        return factors
    return set()