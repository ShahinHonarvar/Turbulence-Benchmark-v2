def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return int(str(n)[:-1])

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    result = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp = truncate_left(temp)
            if temp > 0:
                temp = truncate_right(temp)
        else:
            result.append(num)
    return sorted(result, reverse=True)