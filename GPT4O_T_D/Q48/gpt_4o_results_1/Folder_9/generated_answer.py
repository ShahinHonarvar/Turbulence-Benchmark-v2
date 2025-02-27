def return_binary_or_hexa(nums):
    if len(nums) <= 200:
        return ''
    a = nums[70]
    b = nums[200]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[71:200]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]