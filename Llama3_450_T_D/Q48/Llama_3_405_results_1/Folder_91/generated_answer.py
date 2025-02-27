def return_binary_or_hexa(t):
    a, b = (t[0] + 1, t[6] - 1)
    total_sum = sum(set(range(a, b + 1)) - set(t[1:6]))
    if total_sum == 0:
        return ''
    elif total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]