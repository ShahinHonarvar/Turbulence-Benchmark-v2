def find_primes_between_indices(num_list):
    prime_nums = []
    for num in num_list[413:449]:
        flag = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums