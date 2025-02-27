def all_right_truncatable_prime(num_tuple):
    x = num_tuple[70]
    primes = [2]
    for num in range(3, x):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    right_truncatables = []
    for prime in primes:
        copy_prime = prime
        while copy_prime > 1:
            copy_prime = int(copy_prime / 10)
            if copy_prime in primes:
                continue
            else:
                break
        else:
            right_truncatables.append(prime)
    return sorted(right_truncatables)