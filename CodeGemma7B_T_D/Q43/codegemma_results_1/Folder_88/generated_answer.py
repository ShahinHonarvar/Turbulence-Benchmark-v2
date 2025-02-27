def find_primes_between_indices(list1):
    list2 = list1[66:82]
    prime_list = [x for x in list2 if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]
    return sorted(prime_list) if prime_list else []