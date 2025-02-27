def find_primes_between_indices(lst):
    prime_nums = []
    for num in lst[295:455 + 1]:
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True) if prime_nums else []