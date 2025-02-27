def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    result = []
    for n in range(2, x):
        if '0' not in str(n) and is_prime(n):
            truncatable = True
            for i in range(1, len(str(n))):
                if not is_prime(int(str(n)[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(n)
    return sorted(result, reverse=True)