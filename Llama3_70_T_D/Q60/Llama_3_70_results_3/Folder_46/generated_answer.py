def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    result = []
    for i in range(11, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            j = str(i)
            left_truncatable = True
            right_truncatable = True
            for _ in range(len(j) - 1):
                if not is_prime(int(j[1:])):
                    left_truncatable = False
                    break
                j = j[1:]
            j = str(i)
            for _ in range(len(j) - 1):
                if not is_prime(int(j[:-1])):
                    right_truncatable = False
                    break
                j = j[:-1]
            if left_truncatable and right_truncatable:
                result.append(i)
    return sorted(result)