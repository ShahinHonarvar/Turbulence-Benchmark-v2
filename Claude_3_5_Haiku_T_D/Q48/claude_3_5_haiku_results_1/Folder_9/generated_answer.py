def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[70]
    b = tuple_nums[200]
    present_nums = set(tuple_nums[70:201])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in present_nums:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]