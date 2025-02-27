def return_binary_or_hexa(given_tuple):
    a, b = (given_tuple[933], given_tuple[996])
    sum = 0
    for num in range(a + 1, b):
        if num not in given_tuple[933:996 + 1]:
            sum += num
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:] if sum <= 67108863 else bin(sum)[3:]