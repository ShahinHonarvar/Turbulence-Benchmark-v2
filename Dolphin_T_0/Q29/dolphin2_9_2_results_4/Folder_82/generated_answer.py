def gcf_two_nums(list_of_nums):
    num1 = list_of_nums[33]
    num2 = list_of_nums[72]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a