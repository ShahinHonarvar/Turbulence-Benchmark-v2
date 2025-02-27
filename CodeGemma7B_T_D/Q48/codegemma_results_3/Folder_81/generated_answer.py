def return_binary_or_hexa(s):
    i = s[10] + 1
    sum = 0
    while i < s[100]:
        if i not in s[10:100]:
            sum += i
            i += 1
    if sum % 2 == 1:
        return bin(sum)[2:]
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return ''