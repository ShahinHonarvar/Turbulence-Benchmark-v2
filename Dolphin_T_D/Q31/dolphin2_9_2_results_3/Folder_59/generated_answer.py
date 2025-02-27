def if_perfect_num(lst):
    num = lst[2]
    sum_list = []
    for i in range(1, num):
        if num % i == 0:
            sum_list.append(i)
    return sum([i for i in sum_list if i < num]) == num