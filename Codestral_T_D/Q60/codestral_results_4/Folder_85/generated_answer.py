def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[94]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[1:]
                if not is_prime(int(num_str)):
                    break
            else:
                num_str = str(num)
                while len(num_str) > 1:
                    num_str = num_str[:-1]
                    if not is_prime(int(num_str)):
                        break
                else:
                    result.append(num)
    return sorted(result)