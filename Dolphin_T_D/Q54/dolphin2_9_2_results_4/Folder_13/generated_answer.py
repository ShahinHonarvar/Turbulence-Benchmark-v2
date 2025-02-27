def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(lst):
    x = lst[783]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            prune = str(num)
            for _ in range(len(prune) - 1):
                prune = prune[:-1]
                if not is_prime(int(prune)):
                    break
                if len(prune) == 0:
                    primes.append(num)
    return sorted(primes)