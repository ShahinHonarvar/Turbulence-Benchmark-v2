def find_primes_between_indices(numbers_list):
    prime_numbers = []
    if 261 <= len(numbers_list) <= 459:
        for number in numbers_list[261:460]:
            if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
                prime_numbers.append(number)
    return sorted(prime_numbers)