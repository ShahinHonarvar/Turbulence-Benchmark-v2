def return_binary_or_hexa(tuple_input):
    a = tuple_input[80]
    b = tuple_input[200]
    missing_nums = set(range(a + 1, b))
    for num in tuple_input[80:201]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    missing_sum = sum(missing_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]