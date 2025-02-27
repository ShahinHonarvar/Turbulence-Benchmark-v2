def find_primes_between_indices(lst):
    prime_nums = []
    for i in range(1, len(lst) + 1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            prime_nums.append(i)
    prime_nums.sort()
    return prime_nums if prime_nums else []