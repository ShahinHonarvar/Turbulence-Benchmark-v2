def gcf_three_nums(num_lst):
    num1 = num_lst[742]
    num2 = num_lst[888]
    num3 = num_lst[629]
    i = max(num1, num2, num3)
    while i > 1:
        if i % num1 == 0 and i % num2 == 0 and (i % num3 == 0):
            return i
        i -= 1
    return 1