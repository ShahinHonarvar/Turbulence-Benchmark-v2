def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            i_str = str(i)
            for j in range(1, len(i_str)):
                if is_prime(int(i_str[j:])) and is_prime(int(i_str[:j])):
                    primes.append(i)
                    break
    return sorted(primes, reverse=True)