def find_primes_between_indices(lst):
    prime_numbers = []
    for number in lst[38:55]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                prime_numbers.append(number)
    return sorted(prime_numbers, reverse=True)