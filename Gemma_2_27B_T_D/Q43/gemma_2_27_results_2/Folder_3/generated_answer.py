def find_primes_between_indices(data):
    primes = []
    for num in data[80:85]:
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    primes.sort(reverse=True)
    return primes