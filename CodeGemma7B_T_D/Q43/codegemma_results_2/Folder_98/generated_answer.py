def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(1, 3):
        count = 0
        for j in range(2, num_list[i - 1] + 1):
            if num_list[i - 1] % j == 0:
                count += 1
        if count == 1:
            prime_list.append(num_list[i - 1])
    if prime_list == []:
        return []
    else:
        return sorted(prime_list, reverse=True)