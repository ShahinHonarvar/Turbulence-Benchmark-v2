def gcf_two_nums(arr):
    num1 = arr[96]
    num2 = arr[57]
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i