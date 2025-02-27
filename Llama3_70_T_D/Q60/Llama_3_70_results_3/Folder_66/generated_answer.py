def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[25]
    primes = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i):
            left_truncatable = True
            right_truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    left_truncatable = False
                if not is_prime(int(str(i)[:-j])):
                    right_truncatable = False
            if left_truncatable and right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)