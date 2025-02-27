def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(data):
    x = data[52]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            next_i = str(i)
            while next_i:
                if not is_prime(int(next_i)):
                    primes.remove(int(next_i))
                    break
                next_i = next_i[1:]
            if next_i:
                primes.append(i)
    return primes