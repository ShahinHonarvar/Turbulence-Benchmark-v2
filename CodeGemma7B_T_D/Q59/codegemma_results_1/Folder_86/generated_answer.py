def all_left_truncatable_prime(args):
    """I will write the code for this question."""
    tuple_args = tuple(args)
    new_list = [x for x in [a for a in tuple_args if a != 0] if is_left_truncatable_prime(x)]
    new_list.sort(reverse=True)
    return new_list

def is_left_truncatable_prime(num):
    """Will check is left truncatable or not"""
    str_num = str(num)
    if '0' in str_num:
        return False
    for digits in [int(x) for x in str_num]:
        if not is_prime(digits):
            return False
        num = int(str_num[1:])
        str_num = str(num)
    return True

def is_prime(num):
    """Will check if prime or not"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True