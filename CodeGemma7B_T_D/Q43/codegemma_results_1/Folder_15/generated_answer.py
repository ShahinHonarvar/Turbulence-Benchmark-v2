def find_primes_between_indices(int_list):
    prime_nums = []
    for num in int_list[6:8]:
        if all((num % x != 0 for x in range(2, num))):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)