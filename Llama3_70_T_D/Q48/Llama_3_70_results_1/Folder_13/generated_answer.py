def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    numbers = set(range(a + 1, b)) - set(t[46:92])
    total_sum = sum(numbers)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]