def return_binary_or_hexa(nums):
    if len(nums) <= 202:
        return ''
    a = nums[200]
    b = nums[202]
    full_range = set(range(a + 1, b))
    actual_range = set(nums[201:202])
    missing_numbers = full_range - actual_range
    if not missing_numbers:
        return ''
    summation = sum(missing_numbers)
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]