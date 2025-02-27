def return_binary_or_hexa(numbers):
    if len(numbers) <= 91:
        return ''
    a = numbers[13]
    b = numbers[91]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[14:92]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]