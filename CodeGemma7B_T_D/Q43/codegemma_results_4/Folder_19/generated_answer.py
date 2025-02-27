def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for number in list_of_integers[21:98]:
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return sorted(prime_numbers)