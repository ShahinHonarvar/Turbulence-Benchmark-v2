def if_perfect_num(lst):
    if len(lst) > 21:
        num = lst[21]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    else:
        return False