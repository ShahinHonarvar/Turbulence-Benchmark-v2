def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[79]
    missing_numbers = [n for n in range(a + 1, b) if n not in arr[10:80]]
    if missing_numbers:
        sum_of_missing = sum(missing_numbers)
        if sum_of_missing % 2 == 0:
            return hex(sum_of_missing)[2:]
        else:
            return bin(sum_of_missing)[2:]
    else:
        return ''