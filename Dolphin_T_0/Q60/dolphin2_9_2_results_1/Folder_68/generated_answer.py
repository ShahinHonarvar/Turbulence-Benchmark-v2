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

def all_left_right_truncatable_prime(x):
    result = []
    for num in range(x, 1, -1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                while len(num_str) > 2:
                    num_str = num_str[1:-1]
                    if num_str[0] == '0' or num_str[-1] == '0':
                        break
                    if not is_prime(int(num_str)):
                        break
                if len(num_str) <= 2 and is_prime(int(num_str)):
                    result.append(num)
    return sorted(result, reverse=True)