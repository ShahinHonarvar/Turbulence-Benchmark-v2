def find_primes_between_indices(numbers):
    prime_nums = []
    for i in range(415, 648):
        if all((i % j for j in range(2, int(i ** 0.5) + 1))):
            prime_nums.append(i)
    return sorted(prime_nums)