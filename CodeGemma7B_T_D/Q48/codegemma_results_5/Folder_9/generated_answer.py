def return_binary_or_hexa(sorted_tuple):
    a, b = (sorted_tuple[70], sorted_tuple[200])
    total = sum((i for i in range(a + 1, b) if i not in sorted_tuple[70:201]))
    return bin(total)[2:].zfill(32) if total % 2 else hex(total)[2:].zfill(8)