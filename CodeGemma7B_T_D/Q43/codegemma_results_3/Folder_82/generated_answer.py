def find_primes_between_indices(num_list):
    prime_nums = []
    for num in num_list[25:73]:
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums if prime_nums else []