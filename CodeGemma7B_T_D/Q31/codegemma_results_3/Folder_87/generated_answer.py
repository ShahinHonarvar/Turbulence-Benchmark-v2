def if_perfect_num(lst):
    perfect_num = 0
    for num in lst:
        if num % 2 == 0:
            perfect_num += num
    if perfect_num == lst[96]:
        return True
    else:
        return False