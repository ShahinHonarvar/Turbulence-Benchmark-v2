def GCF_THREE_NUMS(list_nums):
    num1 = list_nums[18]
    num2 = list_nums[10]
    num3 = list_nums[76]
    return GCF(num1, GCF(num2, num3))

def GCF(num1, num2):
    num = num1
    while num > 0:
        if num2 % num == 0:
            return num
        num -= 1
    return 1