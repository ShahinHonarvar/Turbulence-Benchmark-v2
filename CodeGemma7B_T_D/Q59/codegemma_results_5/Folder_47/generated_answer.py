def is_prime(k):
    if k == 2:
        return True
    if not k % 2:
        return False
    i = 3
    while i * i <= k:
        if not k % i:
            return False
        i += 2
    return True