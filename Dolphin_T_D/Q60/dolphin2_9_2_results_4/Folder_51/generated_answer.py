def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    while n:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def all_left_right_truncatable_prime(numbers):
    n = numbers[54]
    primes = []
    for i in range(1, n + 1):
        if is_truncatable(i) and is_prime(i):
            primes.append(i)
    for _ in range(len(primes)):
        temp = primes[0]
        if len(str(temp)) == 1 or len(str(temp)) == 2:
            primes.remove(temp)
        elif is_truncatable(int(str(temp)[1:])) and is_prime(int(str(temp)[1:])) and is_truncatable(int(str(temp)[:-1])) and is_prime(int(str(temp)[:-1])):
            continue
        else:
            primes.remove(temp)
    return sorted(primes)