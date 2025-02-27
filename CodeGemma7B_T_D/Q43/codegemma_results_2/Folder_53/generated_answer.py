def find_primes_between_indices(int_list):
    prime_nums_list = []
    for num in int_list[43:60]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_nums_list.append(num)
    return sorted(prime_nums_list, reverse=True) if prime_nums_list else []