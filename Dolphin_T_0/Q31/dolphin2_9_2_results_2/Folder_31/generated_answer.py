def if_perfect_num(lst):
    sum = 0
    num = lst[66]
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False