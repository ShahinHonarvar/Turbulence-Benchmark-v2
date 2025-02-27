def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            if '0' not in str(i):
                num = str(i)
                while len(num) > 1:
                    if not is_prime(int(num)):
                        break
                    num = num[1:-1]
                else:
                    result.append(i)
    return sorted(result)