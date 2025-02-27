def return_binary_or_hexa(nums):
    a = nums[43]
    b = nums[70]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[43:71]))
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()