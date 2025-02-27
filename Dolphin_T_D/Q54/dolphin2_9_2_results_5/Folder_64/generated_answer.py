import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(num_list, x):
    right_truncatable_list = []
    for x_right in range(2, x):
        if is_prime(x_right):
            truncate = str(x_right)
            tow_truncate = truncate[:-1]
            while len(tow_truncate) >= 1:
                if is_prime(int(tow_truncate)):
                    tow_truncate = tow_truncate[:-1]
                else:
                    break
            else:
                right_truncatable_list.append(x_right)
    return sorted(right_truncatable_list)