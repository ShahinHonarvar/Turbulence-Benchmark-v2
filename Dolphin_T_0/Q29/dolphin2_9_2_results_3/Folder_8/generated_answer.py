def gcf_two_nums(arr):
    num1 = arr[69]
    num2 = arr[41]
    if num1 > num2:
        num1, num2 = (num2, num1)
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i