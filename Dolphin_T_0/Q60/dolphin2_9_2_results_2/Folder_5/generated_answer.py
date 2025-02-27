def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[55]
    res = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' not in num_str:
            left_trunc = num_str[1:]
            right_trunc = num_str[:-1]
            while left_trunc and right_trunc:
                if is_prime(int(left_trunc)) and is_prime(int(right_trunc)):
                    res.append(num)
                    break
                else:
                    left_trunc = left_trunc[1:]
                    right_trunc = right_trunc[:-1]
    return sorted(res)