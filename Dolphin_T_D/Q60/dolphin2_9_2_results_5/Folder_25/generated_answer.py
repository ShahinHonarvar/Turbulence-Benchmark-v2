def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    primes = []
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        for j in range(len(str(i)) - 1, 0, -1):
            if len(str(i)) <= 2 or (is_prime(int(str(i)[1:-1])) and is_prime(int(str(i)[j - 1]))):
                primes.append(i)
    return sorted(primes)