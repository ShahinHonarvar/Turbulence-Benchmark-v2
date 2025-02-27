def if_perfect_num(array):
    if len(array) < 19:
        return False
    num = array[18]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num % (num / i) == 0:
                sum_div = sum_div + i + num / i
            else:
                sum_div = sum_div + i
            i += 1
    return sum_div == num