def find_primes_between_indices(list_of_numbers):
    prime_numbers = []
    for number in list_of_numbers[87:89 + 1]:
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    break
            else:
                prime_numbers.append(number)
    return sorted(prime_numbers)