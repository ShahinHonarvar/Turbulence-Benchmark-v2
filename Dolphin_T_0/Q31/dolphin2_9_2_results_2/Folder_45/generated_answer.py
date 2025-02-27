def if_perfect_num(lst):
    num_33 = lst[33]
    if num_33 < 6:
        return False
    else:
        sum = 1
        for i in range(2, num_33):
            if num_33 % i == 0:
                sum += i
        if sum == num_33:
            return True
        else:
            return False