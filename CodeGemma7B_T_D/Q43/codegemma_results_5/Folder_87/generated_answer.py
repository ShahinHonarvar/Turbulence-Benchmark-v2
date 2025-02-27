def find_primes_between_indices(list_of_ints):
    prime_numbers = []
    for i in range(11, 42):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    prime_numbers.sort(reverse=True)
    return prime_numbers if prime_numbers else []