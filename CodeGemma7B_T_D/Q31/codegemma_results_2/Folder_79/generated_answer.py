def if_perfect_num():
    if list[63] % 6 == 0 or list[63] % 9 == 0:
        return True
    for num in list:
        if num % list[63] == 0:
            return False
    return True