def return_binary_or_hexa(t):
    a = t[10]
    b = t[100]
    expected_sum = (b - a) * (b - a + 1) // 2
    actual_sum = sum(t[11:100])
    diff = actual_sum - expected_sum
    if all((i in t for i in range(a + 1, b))):
        return ''
    elif diff % 2:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]