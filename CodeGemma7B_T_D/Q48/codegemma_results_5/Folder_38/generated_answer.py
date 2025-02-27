def return_binary_or_hexa(nums):
    a, b = (nums[36], nums[85])
    sum_calc = sum((i for i in range(a + 1, b) if i not in nums[36:86]))
    result = '0b' + format(sum_calc, 'b') if sum_calc % 2 else '0x' + format(sum_calc, 'x')
    return result