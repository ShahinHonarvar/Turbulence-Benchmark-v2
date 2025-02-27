def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(args):
    x = args[26]
    primes = [2, 3, 5, 7]
    for i in range(10, x):
        if is_prime(i) and (not '0' in str(i)):
            for j in range(len(str(i)) - 1, 0, -1):
                if not is_prime(int(str(i)[j:])):
                    break
            else:
                primes.append(i)
    return primes