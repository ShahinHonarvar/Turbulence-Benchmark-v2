def find_primes_between_indices(numbers):
    primes = sorted(filter(lambda x: all((x % y != 0 for y in range(2, int(x ** 0.5) + 1))), numbers[31:93]), reverse=True)
    return primes