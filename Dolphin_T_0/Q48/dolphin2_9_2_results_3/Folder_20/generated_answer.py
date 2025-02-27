def return_binary_or_hexa(arr):
    a = arr[27]
    b = arr[96]
    present_numbers = set(arr[27:97])
    total = sum(set(range(a + 1, b)) - present_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()