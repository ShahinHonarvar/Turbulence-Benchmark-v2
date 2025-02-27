def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[41]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                left_str = str_i[1:]
                while left_str and is_prime(int(left_str)):
                    left_str = left_str[1:]
                right_str = str_i[:-1]
                while right_str and is_prime(int(right_str)):
                    right_str = right_str[:-1]
                if (not left_str or is_prime(int(left_str))) and (not right_str or is_prime(int(right_str))):
                    result.append(i)
    return result