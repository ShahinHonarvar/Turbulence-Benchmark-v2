def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    missing_numbers = [x for x in range(a + 1, b) if x not in nums[73:85]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]