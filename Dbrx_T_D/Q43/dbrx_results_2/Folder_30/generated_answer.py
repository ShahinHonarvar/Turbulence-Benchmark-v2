def find_primes_between_indices(numbers):
    primes = sorted(set([i for i in numbers[60:81] if all((i % j != 0 for j in range(2, i)))]), reverse=True)
    return primes