def return_binary_or_hexa(t):
    a = t[50]
    b = t[92]
    total_sum = 0
    for num in range(a + 1, b):
        if num not in t[50:93]:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]