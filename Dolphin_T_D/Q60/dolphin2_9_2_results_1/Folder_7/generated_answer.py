def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[803]
    res = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            while len(str(num)) > 1:
                if not is_prime(int(str(num)[1:-1])):
                    break
                num = int(str(num)[1:-1])
            if is_prime(num):
                res.append(num)
    return sorted(res)