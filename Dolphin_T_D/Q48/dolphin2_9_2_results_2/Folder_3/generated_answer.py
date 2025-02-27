def return_binary_or_hexa(data):
    a = data[56]
    b = data[88]
    missing_nums = []
    for val in range(data[56] + 1, data[88]):
        if val not in data:
            missing_nums.append(val)
    final_sum = sum(missing_nums)
    if final_sum % 2 == 0:
        return hex(final_sum)[2:]
    else:
        return bin(final_sum)[2:]