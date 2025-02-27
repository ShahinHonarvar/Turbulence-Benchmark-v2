def return_binary_or_hexa(tu):
    sum = 0
    for i in range(tu[0] + 1, tu[10]):
        if i not in tu[0:10]:
            sum += i
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()