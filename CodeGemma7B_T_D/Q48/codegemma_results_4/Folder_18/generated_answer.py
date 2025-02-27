def return_binary_or_hexa(tp):
    sum = 0
    for i in range(57, len(tp)):
        sum += tp[i]
    for i in range(91):
        if i not in tp:
            sum += i
    return bin(sum) if sum % 2 else hex(sum)