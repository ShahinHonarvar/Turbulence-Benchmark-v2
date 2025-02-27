def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(20, 49):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)