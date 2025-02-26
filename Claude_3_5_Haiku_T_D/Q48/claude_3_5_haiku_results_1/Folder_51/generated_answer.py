def return_binary_or_hexa(tup):
    a = tup[6]
    b = tup[9]
    absent_nums = [num for num in range(a + 1, b) if num not in tup[6:10]]
    if not absent_nums:
        return ''
    total_sum = sum(absent_nums)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]