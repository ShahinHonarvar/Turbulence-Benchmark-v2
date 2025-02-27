def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i:
            i += 2
        else:
            return False
    return True

def all_left_truncatable_prime(x):
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            tmp = num
            while tmp:
                if not is_prime(tmp):
                    break
                tmp = int(str(tmp)[1:])
            else:
                result.append(num)
    return result