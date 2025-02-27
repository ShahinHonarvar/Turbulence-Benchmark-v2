def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    result = []
    for num in range(2, x + 1):
        if all_left_right_truncatable_prime_helper(num):
            result.append(num)
    return result

def all_left_right_truncatable_prime_helper(num):
    if num < 10 and num != 2 and (num != 3) and (num != 5) and (num != 7):
        return False
    if '0' in str(num):
        return False
    if not is_prime(num):
        return False
    str_num = str(num)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
        if not is_prime(int(str_num[:len(str_num) - i])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True