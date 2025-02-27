def find_primes_between_indices(numbers):
    primes = []
    for i in range(len(numbers)):
        if i >= 17 and i <= 79:
            is_prime = True
            num = numbers[i]
            if num < 2:
                continue
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    if primes:
        return sorted(primes, reverse=True)
    else:
        return []