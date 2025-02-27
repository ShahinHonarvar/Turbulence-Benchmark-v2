def all_left_right_truncatable_prime(int_tuple):
    prime_nums = [i for i in int_tuple if is_prime(i)]
    filtered_nums = [i for i in prime_nums if not has_zero(i)]
    truncatable_nums = []
    for num in filtered_nums:
        if is_truncatable(num):
            truncatable_nums.append(num)
    truncatable_nums.sort(reverse=True)
    return truncatable_nums

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_zero(num):
    return str(num).find('0') != -1

def is_truncatable(num):
    str_num = str(num)
    length = len(str_num)
    for i in range(1, length):
        left, right = (str_num[:i], str_num[i:])
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
    return is_prime(int(str_num)) and is_prime(int(str_num[::-1]))