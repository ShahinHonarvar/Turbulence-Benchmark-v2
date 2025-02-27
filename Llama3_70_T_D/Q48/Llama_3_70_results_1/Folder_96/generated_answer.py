def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[200]
    nums_set = set(nums[51:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]