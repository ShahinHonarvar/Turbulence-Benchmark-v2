def find_primes_between_indices(list_of_integers):
    prime_numbers = []
    for i in range(478, 950):
        number = list_of_integers[i]
        if number == 2:
            prime_numbers.append(number)
        elif number % 2 != 0:
            upper_limit = int(number ** 0.5) + 1
            is_prime = True
            for divisor in range(3, upper_limit, 2):
                if number % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
    prime_numbers.sort(reverse=True)
    return prime_numbers