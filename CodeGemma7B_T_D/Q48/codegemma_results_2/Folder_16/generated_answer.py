def return_binary_or_hexa(tup):
    LTE = tup[90] + 1
    GTE = tup[97] - 1
    sum = 0
    for i in range(LTE, GTE + 1):
        if i not in tup[90:98]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].lower() if sum % 2 != 0 else ''