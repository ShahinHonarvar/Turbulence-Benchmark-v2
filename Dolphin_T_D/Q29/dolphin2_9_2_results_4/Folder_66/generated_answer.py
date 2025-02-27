def gcf_two_nums(num_array):
    num1 = num_array[86]
    num2 = num_array[89]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1