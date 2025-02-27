def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    total_sum = sum(range(a + 1, b))
    existing_sum = sum(nums[26:80])
    diff_sum = total_sum - existing_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 == 0:
        return hex(diff_sum)[2:]
    else:
        return bin(diff_sum)[2:]