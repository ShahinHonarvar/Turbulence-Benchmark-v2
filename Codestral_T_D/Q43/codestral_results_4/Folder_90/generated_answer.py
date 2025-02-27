def find_primes_between_indices(numbers):
    primes = []
    for i in range(413, 449):
        if i < len(numbers):
            num = numbers[i]
            is_prime = True
            if num < 2:
                is_prime = False
            else:
                for j in range(2, int(num ** 0.5) + 1):
                    if num % j == 0:
                        is_prime = False
                        break
            if is_prime:
                primes.append(num)
    return sorted(primes)