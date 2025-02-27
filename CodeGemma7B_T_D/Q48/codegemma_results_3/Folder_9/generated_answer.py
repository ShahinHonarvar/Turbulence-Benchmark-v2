def return_binary_or_hexa(array):
    total = 0
    for num in range(array[70] + 1, array[200]):
        if num not in array[70:201]:
            total += num
    return bin(total)[2:] if total % 2 else hex(total)[2:].lower() if total % 2 else ''