def if_perfect_num(lst):
    if len(lst) > 96:
        target_num = lst[96]
        return sum((factor for factor in range(1, target_num) if target_num % factor == 0)) == target_num
    else:
        return False