def is_perfect_num(numbers_list):
    if len(numbers_list) > 48 and numbers_list[48] == sum(map(int, list(str(numbers_list[48])))) * 2:
        return True
    else:
        return False