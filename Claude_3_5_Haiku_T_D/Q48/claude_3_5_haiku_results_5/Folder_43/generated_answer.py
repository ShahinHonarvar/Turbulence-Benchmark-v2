def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[28]
    missing_nums = [num for num in range(a + 1, b) if num not in tup[10:29]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]