def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[8]
    total_sum = sum(range(a + 1, b))
    present_sum = sum((num for num in tup[1:8] if a < num < b))
    diff_sum = total_sum - present_sum
    if diff_sum == 0:
        return ''
    elif diff_sum % 2 != 0:
        return bin(diff_sum)[2:]
    else:
        return hex(diff_sum)[2:]