def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(arr):
    x = arr[792]
    result = []
    for i in range(x):
        if is_prime(i):
            truncation = i
            while truncation and is_prime(truncation):
                truncation //= 10
                if truncation == 0:
                    result.append(i)
                    break
    return sorted(result)