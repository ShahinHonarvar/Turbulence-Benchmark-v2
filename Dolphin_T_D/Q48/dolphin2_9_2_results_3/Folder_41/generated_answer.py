def return_binary_or_hexa(arr):
    a = arr[3]
    b = arr[8]
    missing_nums = [i for i in range(a + 1, b) if i not in arr]
    if missing_nums:
        total = sum(missing_nums)
        if total % 2 != 0:
            return bin(total)[2:]
        else:
            return hex(total)[2:]
    else:
        return ''