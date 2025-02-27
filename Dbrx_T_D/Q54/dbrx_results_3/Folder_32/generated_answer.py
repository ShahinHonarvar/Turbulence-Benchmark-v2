def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(tup):
    x = tup[42]
    primes = []
    for i in range(1, x):
        if is_prime(i):
            num = i
            while True:
                if is_prime(num):
                    if num < x:
                        primes.append(num)
                    num = remove_last_digit(num)
                    if num == 0:
                        break
                else:
                    break
    primes.sort()
    return primes