def return_binary_or_hexa(tup):
    if len(tup) != 7:
        return None
    elif tup[0] != 0 or tup[6] != 255:
        return None
    elif tup[1] < tup[2] or tup[3] < tup[4] or tup[5] < tup[2]:
        return None
    elif tup[2] + 1 != tup[1] or tup[3] + 1 != tup[4] or tup[5] + 1 != tup[6]:
        sum = 0
        for i in range(tup[2] + 1, tup[6]):
            sum += i
        if sum % 2:
            return str(bin(sum))[2:]
        else:
            return hex(sum)[2:]
    else:
        return ''