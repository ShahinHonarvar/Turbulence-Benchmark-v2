def find_primes_between_indices(num):
    prime_nums = []
    for i in range(1, 6):
        if num[i] == 2 or (num[i] % 2 != 0 and 3 <= num[i] <= 5) or (num[i] % 3 != 0 and num[i] % 5 != 0):
            prime_nums.append(num[i])
    return sorted([num for num in prime_nums])