def find_primes_between_indices(num_list):
    prime_list = []
    for num in num_list[1:3]:
        if num == 2:
            prime_list.append(num)
        elif num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0):
            prime_list.append(num)
    return sorted(prime_list, reverse=True)