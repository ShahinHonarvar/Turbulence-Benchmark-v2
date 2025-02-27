def find_primes_between_indices(numbers):
    prime_numbers = []
    for i in range(5, 9):
        number = numbers[i]
        is_prime = True
        if number < 2:
            is_prime = False
        else:
            for j in range(2, int(number ** 0.5) + 1):
                if number % j == 0:
                    is_prime = False
                    break
        if is_prime:
            prime_numbers.append(number)
    prime_numbers.sort(reverse=True)
    return prime_numbers