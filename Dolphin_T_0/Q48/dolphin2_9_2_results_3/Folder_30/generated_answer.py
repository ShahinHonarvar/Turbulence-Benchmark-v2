def return_binary_or_hexa(arr):
    if not 0 <= 22 < 24 < len(arr) or len(set(arr)) != len(arr):
        return ''
    a, b = (arr[22], arr[24])
    if sorted(arr[22:25]) == list(range(a, b + 1)):
        return ''
    total = sum(set(range(a + 1, b)) - set(arr[23:24]))
    if total & 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()