def if_perfect_num(list1):
    sum = 0
    for i in range(1, list1[8]):
        if list1[8] % i == 0:
            sum = sum + i
    if sum == list1[8]:
        return True
    else:
        return False