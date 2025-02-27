def find_primes_between_indices(list_of_num):
    prime_nums = []
    for num in list_of_num[60:96]:
        is_prime = True
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums