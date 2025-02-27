def find_primes_between_indices(lst):
    prime_numbers = []
    for number in lst:
        if number >= 2:
            is_prime = True
            for divisor in range(2, number):
                if number % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
    prime_numbers.sort()
    return prime_numbers if prime_numbers else []