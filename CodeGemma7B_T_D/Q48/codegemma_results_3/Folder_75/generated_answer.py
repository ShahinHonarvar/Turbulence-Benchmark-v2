def return_binary_or_hexa(T):
    a, b = (T[20], T[51])
    missing_int_sum = 0
    for i in range(a + 1, b):
        if i not in T[20:52]:
            missing_int_sum += i
    if missing_int_sum % 2:
        return bin(missing_int_sum)[2:]
    else:
        return hex(missing_int_sum)[2:].upper()