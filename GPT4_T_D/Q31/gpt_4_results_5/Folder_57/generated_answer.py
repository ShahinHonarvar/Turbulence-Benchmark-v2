def if_perfect_num(lst):
    num = lst[92]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        return True
    else:
        return False