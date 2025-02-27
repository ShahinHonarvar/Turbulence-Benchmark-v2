def return_binary_or_hexa(t):
    a, b = (t[60], t[200])
    present_numbers = set(t[60:201])
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_of_missing_numbers % 2:
        result = bin(sum_of_missing_numbers)[2:]
    else:
        result = hex(sum_of_missing_numbers)[2:]
        result = result.upper() if 'A' <= result <= 'F' else result.lower()
    if len(result) > 1 and result[0] == '0':
        result = result[1:]
    return result