def return_binary_or_hexa(tup):
    for i in range(13, 71):
        if i not in tup[13:71]:
            global sum
            sum += i
    if sum % 2 == 1:
        return str(bin(sum))[2:]
    else:
        return hex(sum)[2:].upper() if str(hex(sum))[2:].upper() <= '9' else str(hex(sum))[2:].lower()