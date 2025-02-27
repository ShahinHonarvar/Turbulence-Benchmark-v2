def find_primes_between_indices(numbers):
    primes = []
    for i in range(38, 55):
        current_number = numbers[i]
        if current_number > 1:
            is_prime = True
            for j in range(2, int(current_number ** 0.5) + 1):
                if current_number % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(current_number)
    return sorted(primes, reverse=True)