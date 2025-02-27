def find_primes_between_indices(input_list):
    prime_list = []
    for num in range(478, 950):
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    return sorted(prime_list, reverse=True)