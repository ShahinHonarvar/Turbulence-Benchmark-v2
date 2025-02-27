def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    required_numbers = set(range(a + 1, b))
    present_numbers = set(nums[31:200])
    missing_numbers = required_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]