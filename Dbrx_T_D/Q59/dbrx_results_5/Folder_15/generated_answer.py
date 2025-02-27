def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def remove_leading_digit(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(t):
    x = t[6]
    result = []
    for num in range(1, x):
        if is_prime(num):
            num_str = str(num)
            num_left_truncatable = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    num_left_truncatable = False
                    break
            if num_left_truncatable:
                result.append(num)
    return sorted(result, reverse=True)