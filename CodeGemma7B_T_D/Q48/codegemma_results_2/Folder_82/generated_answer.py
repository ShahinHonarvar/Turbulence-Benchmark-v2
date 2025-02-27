def return_binary_or_hexa(arg_tuple):
    low = arg_tuple[20] + 1
    high = arg_tuple[200]
    present = set(arg_tuple[20:200])
    sum_to_process = 0
    for i in range(low, high + 1):
        if i not in present:
            sum_to_process += i
    if sum_to_process % 2 == 0:
        return hex(sum_to_process)[2:].upper()
    return bin(sum_to_process)[2:]