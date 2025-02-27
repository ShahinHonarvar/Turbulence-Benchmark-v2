def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):

    def helper(x):
        if x == 0:
            return True
        if x % 10 == 0 or not is_prime(x):
            return False
        return helper(x // 10)
    if is_prime(n) and helper(n):
        return True
    return False

def all_right_truncatable_prime(arr):
    x = arr[88]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)