def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    total_sum = sum(range(a + 1, b))
    actual_sum = sum((num for num in nums[20:32] if a < num < b))
    diff_sum = total_sum - actual_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 == 1:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]