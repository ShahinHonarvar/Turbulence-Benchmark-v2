def return_binary_or_hexa(a, b, data):
    new_list = sorted(set(range(a + 1, b)) - set(data[69:98]))
    sum_nums = sum(new_list)
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].lower() if sum_nums % 2 else ''