def if_perfect_num(arr):
    num = arr[849]
    sum_div = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            sum_div += i
    return sum_div == num