def find_primes_between_indices(int_list):
    prime_list = []
    for i in range(61, 80):
        number = int_list[i]
        for j in range(2, i):
            if number % j == 0:
                break
        else:
            prime_list.append(number)
    return sorted(prime_list) if prime_list else []