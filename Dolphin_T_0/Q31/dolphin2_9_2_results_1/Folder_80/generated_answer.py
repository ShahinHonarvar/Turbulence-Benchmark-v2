def if_perfect_num(lst):
    if len(lst) < 746:
        return False
    else:
        num = lst[746]
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False