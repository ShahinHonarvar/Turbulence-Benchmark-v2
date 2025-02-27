def return_binary_or_hexa(arr):
    try:
        a = arr[50]
        b = arr[200]
    except IndexError:
        return ''
    if a > 1:
        sum_val = sum(range(a, b + 1))
    else:
        sum_val = 0
    for v in arr[51:200]:
        sum_val -= v
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]