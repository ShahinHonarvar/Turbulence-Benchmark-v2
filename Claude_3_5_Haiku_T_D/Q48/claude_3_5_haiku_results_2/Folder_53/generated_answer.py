def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    missing_numbers = [num for num in range(a + 1, b) if num not in nums[200:203]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]