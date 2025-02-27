def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[0], num_tuple[6])
    num_set = set(num_tuple[:7])
    num_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if num_sum == 0:
        return ''
    elif num_sum % 2 == 1:
        return bin(num_sum)[2:]
    else:
        return hex(num_sum)[2:]