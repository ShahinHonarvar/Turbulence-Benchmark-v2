def return_binary_or_hexa(tup):
    a = tup[40]
    b = tup[200]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in tup[40:201]:
            total_sum += i
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]