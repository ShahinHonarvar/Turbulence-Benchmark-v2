def return_binary_or_hexa(tuples):
    a = tuples[37]
    b = tuples[43]
    available_numbers = {i for i in range(a + 1, b)}
    sum = 0
    for i in range(37, 44):
        if tuples[i] in available_numbers:
            available_numbers.remove(tuples[i])
    if not available_numbers:
        return ''
    for i in available_numbers:
        sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]