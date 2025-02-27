def if_perfect_num(array):
    index100 = array[100]
    sum_div = 0
    for i in range(index100):
        if index100 % i == 0:
            sum_div += i
    if sum_div == index100:
        return True
    else:
        return False