def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    existing = numbers[70:201]
    missing = [i for i in range(a + 1, b) if i not in existing]
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
    if not missing:
        return ''