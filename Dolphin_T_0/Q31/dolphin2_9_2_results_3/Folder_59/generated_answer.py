def if_perfect_num(lst):
    perfect_num = lst[2]
    sum = 1
    for i in range(2, perfect_num):
        if perfect_num % i == 0:
            sum = sum + i
    return sum == perfect_num