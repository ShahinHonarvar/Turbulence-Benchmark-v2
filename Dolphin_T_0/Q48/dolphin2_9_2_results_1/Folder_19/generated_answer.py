def return_binary_or_hexa(left_right):
    a = left_right[1]
    b = left_right[4]
    missing = [num for num in range(a + 1, b) if num not in left_right]
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()