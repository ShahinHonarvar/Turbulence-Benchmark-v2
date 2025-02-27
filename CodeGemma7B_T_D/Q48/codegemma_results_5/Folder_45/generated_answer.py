def return_binary_or_hexa(t):
    a, b = (t[30], t[200])
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in t[::80]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()