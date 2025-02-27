def is_perfect_num(num):
    if num % 1 == 0 and num % 2 ** num - 1 == 0:
        return True
    else:
        return False