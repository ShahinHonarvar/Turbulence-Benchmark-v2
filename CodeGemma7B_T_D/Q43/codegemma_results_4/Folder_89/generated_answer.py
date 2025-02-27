def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(69, 85):
        number = list_of_integers[i]
        is_prime = True
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    prime_numbers.sort(reverse=True)
    return prime_numbers