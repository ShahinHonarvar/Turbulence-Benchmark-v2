def find_primes_between_indices(int_list):
    prime_list = []
    for num in int_list[33:60]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list if prime_list else []