def all_left_right_truncatable_prime(x):
    if x < 10 or '0' in str(x):
        return []

    def is_prime(num):
        if num == 2 or num in [i for i in range(3, int(num ** 0.5) + 1, 2)]:
            return True
        return False

    def left_truncation(num, digits):
        return int(str(num)[:-digits]) if digits > 0 else num

    def right_truncation(num, digits):
        return int(str(num)[-digits:]) if digits > 0 else num
    primes = [num for num in range(2, x + 1) if is_prime(num)]
    result = []
    for prime in primes:
        for digits in range(2, int(prime ** 0.5) + 1):
            left = left_truncation(prime, digits)
            right = right_truncation(prime, digits)
            if left != right and is_prime(left) and is_prime(right):
                result.append(prime)
    return sorted(result, reverse=True)