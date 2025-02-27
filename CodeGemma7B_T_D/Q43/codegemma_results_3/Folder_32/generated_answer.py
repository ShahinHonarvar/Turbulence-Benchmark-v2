def find_primes_between_indices(number_list, start_index=60, end_index=95):
    prime_list = []
    for number in number_list[start_index:end_index + 1]:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
    return sorted(prime_list)