def return_binary_or_hexa(numbers):
    a, b = (numbers[44], numbers[91])
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[44:92]]
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]