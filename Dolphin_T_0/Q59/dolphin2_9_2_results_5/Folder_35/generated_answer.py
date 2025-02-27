def all_left_truncatable_prime(numbers):
    x = numbers[177]
    primes = []
    for possible_prime in range(2, x):
        if is_prime(possible_prime):
            possible_prune = possible_prime
            while possible_prune > 0:
                if possible_prune != possible_prime and (not is_prime(possible_prune)):
                    break
                possible_prune //= 10
            else:
                primes.append(possible_prime)
    primes.sort()
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True