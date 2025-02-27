def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[86]
    result = []
    for num in range(x, 0, -1):
        if is_prime(num):
            i = 1
            while i < len(str(num)) - 1:
                if str(num)[i] == '0':
                    break
                if not is_prime(int(str(num)[i:-i])):
                    break
                i += 1
            else:
                result.append(num)
    return sorted(result, reverse=True)