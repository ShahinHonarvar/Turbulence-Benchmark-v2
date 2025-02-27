def all_left_truncatable_prime(n):
    result = []
    for i in range(2, n):
        str_i = str(i)
        if '0' in str_i:
            continue
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result

def is_left_truncatable_prime(i):
    str_i = str(i)
    for j in range(len(str_i)):
        if not is_prime(int(str_i[j:])):
            return False
    return True

def is_prime(number):
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0:
            return False
        if number % (i + 2) == 0:
            return False
        i += 6
    return True