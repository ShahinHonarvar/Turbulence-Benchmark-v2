def find_primes_between_indices(nums):
    prime_numbers = []
    for i in range(72, 73):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers