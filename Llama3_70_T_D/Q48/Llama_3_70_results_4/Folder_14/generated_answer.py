def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[5])
    missing_nums = [i for i in range(a + 1, b) if i not in nums[2:6]]
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]