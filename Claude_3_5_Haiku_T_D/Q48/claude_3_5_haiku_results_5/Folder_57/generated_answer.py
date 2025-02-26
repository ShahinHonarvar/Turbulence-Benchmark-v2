def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    missing_numbers = [x for x in range(a + 1, b) if x not in nums[25:81]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]