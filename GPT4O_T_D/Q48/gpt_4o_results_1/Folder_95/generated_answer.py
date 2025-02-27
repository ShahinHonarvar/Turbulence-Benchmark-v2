def return_binary_or_hexa(data):
    if len(data) <= 99:
        return ''
    a = data[32]
    b = data[99]
    present_numbers = set(data[33:100])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]