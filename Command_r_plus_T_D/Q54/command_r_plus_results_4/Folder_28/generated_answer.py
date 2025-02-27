def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncate(n):
    return int(str(n)[:-1]) if len(str(n)) > 1 else None

def all_right_truncatable_prime(numbers):
    x = numbers[19]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            while temp is not None:
                if not is_prime(temp):
                    break
                temp = right_truncate(temp)
            if temp is None:
                primes.append(num)
    return sorted(primes)