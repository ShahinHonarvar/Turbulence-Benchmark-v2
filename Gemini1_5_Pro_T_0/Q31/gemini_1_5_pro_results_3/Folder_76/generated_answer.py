def if_perfect_num(list_of_integers):
    if len(list_of_integers) <= 537:
        return False
    target = list_of_integers[537]
    if target <= 1:
        return False
    sum = 1
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            sum += i + target // i
    if sum == target:
        return True
    else:
        return False