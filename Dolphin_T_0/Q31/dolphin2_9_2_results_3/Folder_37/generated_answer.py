def if_perfect_num(lst):
    perfect_sum = 1
    num = lst[28]
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            perfect_sum = perfect_sum + i + num // i
            i += 1
        else:
            perfect_sum = perfect_sum + i
            i += 1
    if perfect_sum == num and num != 1:
        return True
    else:
        return False