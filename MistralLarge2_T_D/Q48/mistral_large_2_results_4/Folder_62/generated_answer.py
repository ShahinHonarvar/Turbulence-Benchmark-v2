def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    range_sum = sum(set(range(a + 1, b)) - set(nums[50:93]))
    if range_sum == 0:
        return ''
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:].upper()