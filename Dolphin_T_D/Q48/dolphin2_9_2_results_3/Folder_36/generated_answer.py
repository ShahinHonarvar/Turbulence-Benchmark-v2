def return_binary_or_hexa(tup):
    start = tup[110]
    end = tup[348]
    true_sum = 0
    for i in range(start + 1, end + 1):
        if i not in tup:
            true_sum += i
    if true_sum % 2 != 0:
        return bin(true_sum)[2:]
    else:
        return hex(true_sum)[2:]