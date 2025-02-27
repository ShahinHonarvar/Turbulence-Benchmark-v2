def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    pb = 3
    while pb * pb <= n and n % pb != 0:
        pb += 2
    if pb * pb > n:
        return True
    return False

def is_truncatable(n, n1):
    return n1 != 0 and is_prime(n1) and is_truncatable(n1, n1 // 10)

def all_left_truncatable_prime(arr):
    x = arr[87]
    left_truncatables = [i for i in range(1, x) if is_prime(i) and is_truncatable(i, i // 10)]
    return sorted(left_truncatables)