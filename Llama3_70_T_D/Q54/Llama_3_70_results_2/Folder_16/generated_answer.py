def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[792]
    rtps = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                rtps.append(i)
    return sorted(rtps)