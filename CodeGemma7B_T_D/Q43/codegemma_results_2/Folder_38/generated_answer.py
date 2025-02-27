def find_primes_between_indices(int_list):
    primes = []
    for number in int_list[55:88]:
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    if len(primes) == 0:
        return []
    else:
        return sorted(primes)