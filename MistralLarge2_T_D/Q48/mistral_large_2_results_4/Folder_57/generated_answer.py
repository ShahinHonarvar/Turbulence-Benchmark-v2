def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    num_set = set(nums[25:81])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()