def return_binary_or_hexa(arr):
    a = arr[34]
    b = arr[69]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in arr:
            missing_numbers.append(i)
    if missing_numbers:
        total = sum(missing_numbers)
        if total % 2 == 0:
            return bin(total)[2:]
        else:
            return hex(total)[2:]
    else:
        return ''