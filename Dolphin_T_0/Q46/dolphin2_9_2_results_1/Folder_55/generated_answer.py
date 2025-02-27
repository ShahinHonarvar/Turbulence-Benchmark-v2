def gcf_three_nums(nums_list):
    num1 = nums_list[9]
    num2 = nums_list[6]
    num3 = nums_list[2]
    gcf = min(num1, num2, num3)
    while True:
        if gcf % num1 == 0 and gcf % num2 == 0 and (gcf % num3 == 0):
            break
        gcf -= 1
    return gcf