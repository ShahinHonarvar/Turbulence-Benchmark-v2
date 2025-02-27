def find_primes_between_indices(numbers: list) -> list:
    prime_nums = []
    for i in range(25, 63):
        if numbers[i] <= 1:
            continue
        is_prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(numbers[i])
    prime_nums.sort()
    return prime_nums