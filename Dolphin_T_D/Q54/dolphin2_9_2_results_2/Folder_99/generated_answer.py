def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[758]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            r = str(num)
            while len(r) != 0:
                if not is_prime(int(r)):
                    break
                r = r[0:-1]
                if len(r) == 0:
                    primes.append(num)
    return sorted(primes)