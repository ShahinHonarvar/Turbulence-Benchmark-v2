def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[34:78]]
    total = sum(missing_numbers)
    if missing_numbers:
        return bin(total)[2:] if total % 2 else hex(total)[2:]
    else:
        return ''