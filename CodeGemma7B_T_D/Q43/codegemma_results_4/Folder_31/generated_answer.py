def find_primes_between_indices(lst):
    prime_nums = []
    for num in lst[37:96]:
        if num <= 1:
            continue
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)