def return_binary_or_hexa(arr):
    a = arr[38]
    b = arr[52]
    missing = [x for x in range(a + 1, b) if x not in arr]
    sum = 0 if not missing else sum(missing)
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]