def if_perfect_num(lst):
    num = lst[72]
    sum_ = 0
    for i in range(1, num):
        if num % i == 0:
            sum_ += i
    return num == sum_