def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in nums[16:88]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]