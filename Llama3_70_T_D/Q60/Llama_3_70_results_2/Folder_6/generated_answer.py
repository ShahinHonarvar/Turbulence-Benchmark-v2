def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            left, right = (str(num), str(num))
            while len(left) > 2:
                left, right = (left[1:], right[:-1])
                if not is_prime(int(left)) or not is_prime(int(right)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(num)
    return sorted(primes)