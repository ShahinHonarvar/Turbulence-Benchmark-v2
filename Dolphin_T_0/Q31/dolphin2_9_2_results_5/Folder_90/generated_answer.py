def if_perfect_num(lst):
    perfect_num = 0
    target_num = lst[263]
    for i in range(1, int(target_num ** 0.5) + 1):
        if target_num % i == 0:
            perfect_num += i
            if target_num // i != i:
                perfect_num += target_num // i
    if perfect_num == target_num:
        return True
    else:
        return False