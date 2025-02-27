def find_primes_between_indices(numbers):
    primes = sorted(set((number for number in numbers[14:74] if number > 1 and all((number % divisor != 0 for divisor in range(2, number))))))
    return primes[::-1] if primes else []