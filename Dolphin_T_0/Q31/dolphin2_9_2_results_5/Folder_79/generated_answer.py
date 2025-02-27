def if_perfect_num(lst):
    num = lst[63]
    if num == 0:
        return False
    else:
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        else:
            return False