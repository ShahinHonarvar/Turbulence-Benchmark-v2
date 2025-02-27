def find_primes_between_indices(data):
    primes = []
    for i in range(1, 6):
        num = data[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)