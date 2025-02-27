def return_binary_or_hexa(numbers):
    if len(numbers) <= 200:
        return ''
    a = numbers[80]
    b = numbers[200]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[81:200]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]