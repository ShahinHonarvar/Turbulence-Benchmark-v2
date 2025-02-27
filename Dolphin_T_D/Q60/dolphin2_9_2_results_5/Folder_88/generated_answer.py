def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[93]
    numbers = [i for i in range(1, x + 1) if is_prime(i)]
    res = []
    for i in numbers:
        left, right = (i, i)
        while left > 9 and right > 9:
            left = left // 10
            right = right % 10
            if left < 10 and right < 10 and is_prime(left) and is_prime(right):
                res.append(i)
                break
    return sorted(res)