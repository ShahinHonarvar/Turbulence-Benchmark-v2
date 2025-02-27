def find_primes_between_indices(int_list):
    prime_list = []
    for num in int_list[38:55]:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    return sorted(prime_list, reverse=True) if prime_list else []