def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(l):
    x = l[758]
    primes = []
    for i in range(x, 9999, -1):
        if is_prime(i) and (not '0' in str(i)) and (len(str(i)) > 1):
            i = str(i)
            while len(i) > 1:
                if not is_prime(int(i[1:-1])):
                    break
                i = i[1:-1]
            if len(i) == 1 and is_prime(int(i)):
                primes.append(int(i))
    return sorted(primes)