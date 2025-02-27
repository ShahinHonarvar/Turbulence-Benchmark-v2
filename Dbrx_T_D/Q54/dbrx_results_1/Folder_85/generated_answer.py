def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(t):
    x = t[94]
    result = []
    for num in range(2, x):
        if is_prime(num):
            current_num = num
            while current_num > 0:
                if not is_prime(current_num):
                    break
                current_num = remove_last_digit(current_num)
            else:
                result.append(num)
    return sorted(result)