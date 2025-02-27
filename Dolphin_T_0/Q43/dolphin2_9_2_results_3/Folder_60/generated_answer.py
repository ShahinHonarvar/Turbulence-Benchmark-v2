def find_primes_between_indices(lst):
    prime_numbers = []
    for number in lst[46:86]:
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
    return sorted(prime_numbers)