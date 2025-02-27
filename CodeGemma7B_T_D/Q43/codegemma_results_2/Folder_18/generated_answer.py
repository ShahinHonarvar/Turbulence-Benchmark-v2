def find_primes_between_indices(num_list):
    prime_nums = []
    for num in num_list[430:806]:
        if num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums