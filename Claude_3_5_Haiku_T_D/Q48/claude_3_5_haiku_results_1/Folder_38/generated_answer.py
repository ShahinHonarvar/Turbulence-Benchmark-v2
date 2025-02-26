def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[36:86]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 == 1 else hex(total_sum)[2:]