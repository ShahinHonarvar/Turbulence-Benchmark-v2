def if_perfect_num(lst):
    if len(lst) < 460:
        return False
    num = lst[459]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num