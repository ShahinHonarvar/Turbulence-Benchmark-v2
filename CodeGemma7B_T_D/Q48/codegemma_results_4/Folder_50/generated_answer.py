def return_binary_or_hexa(tuple):
    start = tuple[13] + 1
    end = tuple[76]
    sum = 0
    for num in range(start, end + 1):
        if num not in tuple[13:76]:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()