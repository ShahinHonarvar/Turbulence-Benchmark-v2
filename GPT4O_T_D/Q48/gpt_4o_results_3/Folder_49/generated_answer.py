def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    present_numbers = set(numbers[81:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]