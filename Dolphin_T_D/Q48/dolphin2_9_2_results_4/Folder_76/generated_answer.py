def return_binary_or_hexa(tup):
    a = tup[450]
    b = tup[905]
    result_set = set(range(a + 1, b)) - set(tup[450:906])
    result_sum = sum(result_set)
    if len(result_set) == 0:
        return ''
    elif result_sum % 2 == 0:
        return hex(result_sum)[2:]
    else:
        return bin(result_sum)[2:]