def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[60], num_tuple[200])
    summation = 0
    for num in range(a + 1, b):
        if num not in num_tuple[60:201]:
            summation += num
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:].upper()