def all_left_right_truncatable_prime(n):
    result = [2]
    for number in range(3, n + 1, 2):
        if is_prime(number) and '0' not in str(number) and left_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def left_right_truncatable_prime(number):
    if number <= 1 or number >= 10 ** 7:
        return False
    stra = str(number)
    if len(stra) <= 2:
        return True
    for i in range(0, len(stra) - 2):
        res = int(stra[0:len(stra) - i - 1])
        if not is_prime(res):
            return False
    return True