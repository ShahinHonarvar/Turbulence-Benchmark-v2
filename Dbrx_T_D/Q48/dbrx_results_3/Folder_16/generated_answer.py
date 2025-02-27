def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[90]
    b = sorted_tuple[97]
    sum = 0
    if a < b:
        for i in range(a + 1, b):
            if i not in sorted_tuple[90:98]:
                sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()