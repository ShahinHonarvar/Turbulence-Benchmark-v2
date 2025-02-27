def return_binary_or_hexa(nums):
    if nums[87] - nums[42] <= 1:
        return ''
    res = 0
    for i in range(nums[42] + 1, nums[87]):
        if i not in nums:
            res += i
    return bin(res)[2:] if res % 2 else hex(res)[2:].upper()