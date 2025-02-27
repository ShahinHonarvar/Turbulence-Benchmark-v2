def find_primes_between_indices(data):
    Primes = []
    for i in range(61, 81):
        num = data[i]
        is_prime = True
        if num <= 1:
            is_prime = False
        else:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_prime = False
                    break
        if is_prime:
            Primes.append(num)
    Primes.sort(reverse=True)
    return Primes