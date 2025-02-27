def if_perfect_num(lst):
    num = lst[34]
    if num > 0:
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num
    return False