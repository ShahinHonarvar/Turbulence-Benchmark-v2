def find_primes_between_indices(list):
    prime_numbers = []
    for i in range(57, 65):
        is_prime = True
        for j in range(2, int(list[i] ** 0.5) + 1):
            if list[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(list[i])
    return sorted(prime_numbers, reverse=True)