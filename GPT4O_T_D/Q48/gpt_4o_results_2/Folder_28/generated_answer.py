def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    present_numbers = set(nums[87:100])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]