def if_perfect_num(inputs):
    perfect_nums = [6, 28, 496, 8128]
    for num in inputs:
        if num in perfect_nums:
            return True
    return False