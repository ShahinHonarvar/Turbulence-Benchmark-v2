def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i >= 187 and i <= 271:
            is_prime = True
            if numbers[i] < 2:
                is_prime = False
            for j in range(2, int(numbers[i] ** 0.5) + 1):
                if numbers[i] % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(numbers[i])
    return sorted(primes)