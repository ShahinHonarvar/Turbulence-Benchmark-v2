def if_perfect_num(lst):
    num = lst[40]
    return num == sum([i for i in range(1, num) if num % i == 0])