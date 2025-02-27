def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for number in list_of_integers:
        if number <= 1:
            continue
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return sorted(prime_numbers)