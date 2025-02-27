def if_perfect_num(lst):
    num = lst[263]
    if num < 0:
        return False
    else:
        perfect_sum = 1
        for i in range(2, num):
            if num % i == 0:
                perfect_sum += i
        if perfect_sum == num:
            return True
        else:
            return False