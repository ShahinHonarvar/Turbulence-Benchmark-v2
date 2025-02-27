def if_perfect_num(lst):
    num = lst[29]
    perfect_sum = 0
    for i in range(1, num):
        if num % i == 0:
            perfect_sum += i
    return perfect_sum == num