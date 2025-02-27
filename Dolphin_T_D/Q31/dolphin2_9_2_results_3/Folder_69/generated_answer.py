def if_perfect_num(lst):
    index = 459
    num = lst[index]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num