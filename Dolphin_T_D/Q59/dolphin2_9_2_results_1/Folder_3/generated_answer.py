def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[100]
    result = []
    for num in range(2, x):
        if is_prime(num) and (not '0' in str(num)):
            trunc = num
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    result.append(num)
    return sorted(result)