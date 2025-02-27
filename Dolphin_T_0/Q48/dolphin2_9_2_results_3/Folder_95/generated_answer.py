def return_binary_or_hexa(arr):
    a, b = (arr[32], arr[99])
    missing_ints = [i for i in range(a + 1, b) if i not in arr[32:100]]
    total_sum = sum(missing_ints)
    if len(missing_ints) == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]