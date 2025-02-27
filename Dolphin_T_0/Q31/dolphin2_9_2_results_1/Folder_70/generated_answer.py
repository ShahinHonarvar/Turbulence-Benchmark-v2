def is_perfect_num(lst):
    perfect_num = lst[845]
    sum = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum = sum + i
    if sum == perfect_num:
        return True
    else:
        return False