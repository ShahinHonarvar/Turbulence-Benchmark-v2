def find_primes_between_indices(list):
    prime_list = []
    for num in list[459:782]:
        is_prime = True
        if num <= 1:
            is_prime = False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
        if is_prime:
            prime_list.append(num)
    prime_list.sort()
    return prime_list if prime_list else []