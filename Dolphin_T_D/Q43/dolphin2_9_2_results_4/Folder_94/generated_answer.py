def find_primes_between_indices(num_list):
    primes = []
    for i in range(10, 13):
        num = num_list[i]
        if all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes)