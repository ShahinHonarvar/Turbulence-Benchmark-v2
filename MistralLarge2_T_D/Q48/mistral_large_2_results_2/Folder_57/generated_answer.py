def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    sub_tuple = t[25:81]
    missing_sum = sum((i for i in range(a + 1, b) if i not in sub_tuple))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]