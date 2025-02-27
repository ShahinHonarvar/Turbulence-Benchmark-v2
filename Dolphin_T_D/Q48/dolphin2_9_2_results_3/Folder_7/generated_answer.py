def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[97]
    missing = [x for x in range(a + 1, b) if x not in arr]
    if missing:
        sum_ = sum(missing)
        if sum_ % 2 == 0:
            return hex(sum_)[2:]
        else:
            return bin(sum_)[2:]
    else:
        return ''