def find_primes_between_indices(numbers):
    primes = []
    for number in numbers[30:44]:
        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(number)
    return sorted(primes) or []