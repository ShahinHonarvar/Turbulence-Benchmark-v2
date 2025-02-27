def gcf_two_nums(nums_list):
    num1 = nums_list[56]
    num2 = nums_list[92]
    factors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    return max(factors)