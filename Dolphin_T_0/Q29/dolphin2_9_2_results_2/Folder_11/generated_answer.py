def gcf_two_nums(nums):
    num1 = nums[64]
    num2 = nums[80]
    gcf = arr_gcf(num1, num2)
    return gcf

def arr_gcf(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i