def if_perfect_num(lst):
    if len(lst) > 87:
        num = lst[87]
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum = sum + i
        if sum == num:
            return True
    return False