def find_primes_between_indices(prime_list):
    prime_nums = []
    for i in range(459, 782):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_nums.append(i)
    return sorted(prime_nums)