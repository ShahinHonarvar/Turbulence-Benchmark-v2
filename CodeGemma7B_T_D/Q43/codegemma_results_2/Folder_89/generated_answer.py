def find_primes_between_indices(number_list):
    prime_nums = []
    for i in range(69, 85):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            prime_nums.append(i)
    prime_nums.sort(reverse=True)
    return prime_nums