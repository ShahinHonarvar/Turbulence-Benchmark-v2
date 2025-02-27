def find_primes_between_indices(lst):
    prime_nums = []
    for i in range(66, 82):
        num = lst[i]
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    return sorted(prime_nums)