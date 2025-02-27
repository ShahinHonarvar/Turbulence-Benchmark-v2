def if_perfect_num(lst):
    for num in lst:
        if num % 2 == 0:
            sum = num + num / 2
        else:
            sum = num + (2 * num - 1) / 2
    if lst[92] == sum:
        return True
    else:
        return False