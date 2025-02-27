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

def remove_last_digit(n):
    return int(str(n)[:-1])

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[25]
    result = []
    for num in range(10, x):
        if is_prime(num):
            current_num = num
            while current_num != 0:
                if not is_prime(current_num):
                    break
                current_num = remove_last_digit(current_num)
            else:
                result.append(num)
    return sorted(result, reverse=True)