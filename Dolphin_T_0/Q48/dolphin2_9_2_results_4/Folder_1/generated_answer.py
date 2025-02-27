def return_binary_or_hexa(t):
    a, b = (t[17], t[88])
    sum_num = 0
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in t:
            missing_numbers.append(i)
    if missing_numbers:
        sum_num = sum(missing_numbers)
        if sum_num % 2:
            return bin(sum_num)[2:]
        else:
            return hex(sum_num)[2:].upper()
    else:
        return ''