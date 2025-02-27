def return_binary_or_hexa(lst):
    a = lst[275]
    b = lst[871]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in lst[275:872]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]