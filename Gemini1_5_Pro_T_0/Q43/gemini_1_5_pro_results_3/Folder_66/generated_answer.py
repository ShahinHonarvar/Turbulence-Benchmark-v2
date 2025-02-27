def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[43:81]:
        is_prime = True
        if num <= 1:
            is_prime = False
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    return sorted(primes)