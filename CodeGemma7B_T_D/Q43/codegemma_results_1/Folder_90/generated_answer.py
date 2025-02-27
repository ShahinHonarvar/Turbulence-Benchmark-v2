def find_primes_between_indices(int_list):
    result = []
    for num in int_list[412:449]:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return sorted(result) or []