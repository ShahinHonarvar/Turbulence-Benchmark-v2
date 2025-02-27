def return_binary_or_hexa(num_tuple):
    z = {i for i in range(num_tuple[20] + 1, num_tuple[36])}
    sum_missing = sum(z)
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:].upper()