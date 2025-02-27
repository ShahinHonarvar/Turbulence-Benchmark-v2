def if_perfect_num(lst):
    count = 0
    if len(lst) > 87:
        num = lst[87]
        for i in range(1, num):
            if num % i == 0:
                count += i
        return count == num