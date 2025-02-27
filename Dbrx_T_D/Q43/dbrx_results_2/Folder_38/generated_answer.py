def find_primes_between_indices(numbers):
    primes = []
    for i in numbers[55:88]:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
    return sorted(primes)