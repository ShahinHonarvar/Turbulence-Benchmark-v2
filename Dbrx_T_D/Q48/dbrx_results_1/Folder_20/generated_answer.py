def return_binary_or_hexa(arr):
    a, b = (arr[27], arr[96])
    if a + 1 > b - 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(arr[27:97])
    diff = missing_numbers - present_numbers
    if not diff:
        return ''
    summation = sum(diff)
    if summation % 2:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:].upper()