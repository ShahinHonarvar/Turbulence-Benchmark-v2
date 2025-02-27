def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    missing_nums = []
    for num in range(a + 1, b):
        missing_nums.append(num)
    for num in nums[40:201]:
        if num in missing_nums:
            missing_nums.remove(num)
    if len(missing_nums) == 0:
        return ''
    s = sum(missing_nums)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]