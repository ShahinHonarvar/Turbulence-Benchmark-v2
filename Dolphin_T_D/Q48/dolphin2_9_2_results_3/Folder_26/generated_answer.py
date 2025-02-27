def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    if a > b:
        return ''
    specified = [a + 1, b - 1]
    actual = t[68:100]
    diff = [i for i in specified if i not in actual]
    sum = 0
    for i in diff:
        sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]