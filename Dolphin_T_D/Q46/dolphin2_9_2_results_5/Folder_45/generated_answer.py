def gcf_three_nums(lst):
    num1 = lst[46]
    num2 = lst[84]
    num3 = lst[23]
    gcf = 1
    nums = [num1, num2, num3]
    for num in nums:
        for i in range(2, num):
            if num % i == 0:
                gcf = i
                if num % gcf == 0 and num1 % gcf == 0 and (num2 % gcf == 0) and (num3 % gcf == 0):
                    gcf = max(gcf, nums)
    return gcf