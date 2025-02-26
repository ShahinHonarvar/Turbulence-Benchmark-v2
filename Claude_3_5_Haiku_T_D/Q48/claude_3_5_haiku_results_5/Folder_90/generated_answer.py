def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[60]
    b = tuple_nums[90]
    absent_nums = [num for num in range(a + 1, b) if num not in tuple_nums[60:91]]
    if not absent_nums:
        return ''
    total_sum = sum(absent_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]