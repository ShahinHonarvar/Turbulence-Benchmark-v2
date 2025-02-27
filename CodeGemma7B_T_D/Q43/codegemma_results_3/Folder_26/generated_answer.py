def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(23, 49):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return sorted(prime_numbers)