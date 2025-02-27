def if_perfect_num(lst):
    if sum(lst) != 0:
        num = lst[985]
        if num != 0:
            sum = 1
            for i in range(2, num):
                if num % i == 0:
                    sum += i
            if sum == num:
                return True
    return False