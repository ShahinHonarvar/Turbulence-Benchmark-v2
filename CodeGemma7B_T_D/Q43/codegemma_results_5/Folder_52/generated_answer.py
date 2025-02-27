def find_primes_between_indices(num_list):
    prime_nums = [num for num in num_list[33:60] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    prime_nums.sort(reverse=True)
    return prime_nums