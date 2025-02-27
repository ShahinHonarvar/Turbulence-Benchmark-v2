def find_primes_between_indices(list_of_int):
    prime_list = []
    try:
        for i in range(list_of_int[6], list_of_int[7] + 1):
            if i >= 2:
                is_prime = True
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_list.append(i)
        prime_list.sort(reverse=True)
        return prime_list
    except IndexError:
        return []