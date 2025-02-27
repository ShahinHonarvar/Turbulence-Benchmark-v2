def if_perfect_num(arr):
    if len(arr) == 0:
        return False
    num = arr[0]
    div_sum = 1
    for i in range(2, num):
        if num % i == 0:
            div_sum += i
    if div_sum == num:
        return True
    return False