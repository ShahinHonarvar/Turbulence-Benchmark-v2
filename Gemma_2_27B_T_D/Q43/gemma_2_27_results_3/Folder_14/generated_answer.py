def find_primes_between_indices(data):
    primes = []
    for num in data[10:67]:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes)