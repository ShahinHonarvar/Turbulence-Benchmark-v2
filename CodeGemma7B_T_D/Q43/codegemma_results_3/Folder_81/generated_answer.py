def find_primes_between_indices(number_list):
    prime_list = []
    for number in number_list[59:98]:
        is_prime = True
        for divisor in range(2, int(number / 2) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
    prime_list.sort(reverse=True)
    return prime_list