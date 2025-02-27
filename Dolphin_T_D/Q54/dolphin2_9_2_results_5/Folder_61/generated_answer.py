def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[3]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            digit = len(str(i)) - 1
            while digit > 0:
                if not is_prime(int(str(i).replace(str(i)[-digit], ''))):
                    break
                digit -= 1
            else:
                primes.append(i)
    return sorted(primes, reverse=True)