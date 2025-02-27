def return_binary_or_hexa(arr):
    a = arr[10]
    b = arr[100]
    not_in_list = [x for x in range(a + 1, b) if x not in arr]
    if not not_in_list:
        return ''
    res = sum(not_in_list)
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:]