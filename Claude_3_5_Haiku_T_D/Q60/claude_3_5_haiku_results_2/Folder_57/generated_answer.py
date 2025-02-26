def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[54]
    result = []
    for n in range(x, 11, -1):
        if '0' in str(n):
            continue
        is_truncatable = True
        temp = n
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        temp = n
        num_str = str(temp)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(n)
    return result