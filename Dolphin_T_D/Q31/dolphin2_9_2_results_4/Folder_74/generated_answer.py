def if_perfect_num(lst):
    index = 48
    num = lst[index]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num and num != 1