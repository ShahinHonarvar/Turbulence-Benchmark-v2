def find_primes_between_indices(int_list):
    prime_list = []
    for num in int_list[19:86]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_list.append(num)
    return prime_list[::-1]