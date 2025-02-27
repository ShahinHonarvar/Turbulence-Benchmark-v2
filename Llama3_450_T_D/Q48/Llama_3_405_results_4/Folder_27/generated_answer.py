def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    total_sum = sum(range(a + 1, b))
    tuple_sum = sum((i for i in t[87:89] if a < i < b))
    missing_sum = total_sum - tuple_sum
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]