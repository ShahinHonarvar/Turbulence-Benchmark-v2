def find_primes_between_indices(numbers):
    primes = [x for x in numbers[157:736] if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]
    return sorted(primes, reverse=True)