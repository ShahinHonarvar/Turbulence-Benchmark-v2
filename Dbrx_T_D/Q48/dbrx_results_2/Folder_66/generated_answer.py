def return_binary_or_hexa(nums):
    a, b = (nums[11], nums[76])
    non_present = set(range(a + 1, b)) - set(nums[12:76])
    if not non_present:
        return ''
    sum_result = sum(non_present)
    return format(sum_result, 'b') if sum_result % 2 else format(sum_result, 'x')