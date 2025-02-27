def find_primes_between_indices(my_list):
    prime_numbers = []
    for number in my_list[30:44]:
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                prime_numbers.append(number)
    return sorted(prime_numbers)