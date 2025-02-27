def if_perfect_num(lst):
    if len(lst) < 127:
        return False
    else:
        num = lst[126]
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num