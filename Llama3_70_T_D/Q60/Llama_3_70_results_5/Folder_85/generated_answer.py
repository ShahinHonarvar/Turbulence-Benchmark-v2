def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for i in range(11, x + 1):
        if '0' not in str(i) and is_prime(i):
            left = str(i)
            right = str(i)
            while len(left) > 2 and len(right) > 2:
                left = left[1:]
                right = right[:-1]
                if not is_prime(int(left)) or not is_prime(int(right)):
                    break
            else:
                primes.append(i)
    return sorted(primes)