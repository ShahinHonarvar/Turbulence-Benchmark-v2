def find_primes_between_indices(num_list):
    prime_nums = []
    index = 27
    limit = max(num_list)
    while index <= 86:
        num = num_list[index]
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_nums.append(num)
        index += 1
    prime_nums.sort(reverse=True)
    return prime_nums if prime_nums else []