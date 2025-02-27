def if_perfect_num(lst):
    num = lst[67]
    perfect_sum = 1
    for i in range(2, num):
        if num % i == 0:
            perfect_sum += i
    return perfect_sum == num and num != 1