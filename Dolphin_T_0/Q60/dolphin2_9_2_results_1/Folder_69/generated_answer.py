def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[760]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and i % 10 != 0 and (i != 1):
            left = i // 10
            right = i % 10
            while left != 0 and right != 0 and is_prime(left) and is_prime(right):
                i = left
                left = i // 10
                right = i % 10
            if left == 0 and right == 0:
                primes.append(i)
    return sorted(primes, reverse=True)