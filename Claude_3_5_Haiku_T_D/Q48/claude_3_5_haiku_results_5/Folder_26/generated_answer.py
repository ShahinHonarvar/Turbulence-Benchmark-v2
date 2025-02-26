def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[68:100]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 == 1 else hex(total_sum)[2:]