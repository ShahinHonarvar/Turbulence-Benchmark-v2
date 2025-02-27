def return_binary_or_hexa(a_b):
    a, b = (a_b[1], a_b[4])
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in a_b:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].lower()