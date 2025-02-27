def is_perfect_num(num):
    if num % 37 == 0:
        if num % 3 == 0 and num % 7 == 0:
            return True
        else:
            return False