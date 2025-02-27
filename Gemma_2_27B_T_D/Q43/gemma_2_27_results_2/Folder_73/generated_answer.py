def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 91):
        num = numbers[i]
        is_prime = True
        if num <= 1:
            is_prime = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes