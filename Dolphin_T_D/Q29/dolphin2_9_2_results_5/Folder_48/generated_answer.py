def gcf_two_nums(arr):
    num1 = arr[618]
    num2 = arr[195]
    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf