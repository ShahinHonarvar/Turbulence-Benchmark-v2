def find_primes_between_indices(lst):
    prime_list = []
    for i in range(478, 950):
        if lst[i] == 2 or (lst[i] % 2 != 0 and (lst[i] ** 0.5).is_integer() is False):
            prime_list.append(lst[i])
    prime_list.sort(reverse=True)
    return prime_list if prime_list else []