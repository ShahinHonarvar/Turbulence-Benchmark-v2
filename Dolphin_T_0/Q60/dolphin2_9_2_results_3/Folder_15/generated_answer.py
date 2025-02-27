def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[6]
    res = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if '0' not in num_str:
            if is_prime(int(num_str)):
                for i in range(len(num_str) - 2, 0, -1):
                    if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
                        break
                else:
                    res.append(num)
    return res