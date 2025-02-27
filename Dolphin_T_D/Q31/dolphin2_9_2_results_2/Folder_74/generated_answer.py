def if_perfect_num(my_list):
    if len(my_list) < 49:
        return False
    else:
        num = my_list[48]
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum = sum + i
        if sum == num:
            return True
        else:
            return False