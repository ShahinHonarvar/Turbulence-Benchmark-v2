def find_primes_between_indices(numbers):
    primes = []
    for i in range(31, 93):
        number = numbers[i]
        if number > 1:
            is_prime = True
            for j in range(2, int(number ** 0.5) + 1):
                if number % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(number)
    primes.sort(reverse=True)
    return primes