def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    missing = [i for i in range(a + 1, b) if i not in t]
    sum_num = sum(missing)
    if sum_num % 2 != 0:
        return bin(sum_num)[2:]
    else:
        return hex(sum_num)[2:]