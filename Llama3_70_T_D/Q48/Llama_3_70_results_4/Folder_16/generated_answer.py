def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    excluded = set(numbers[90:98])
    total = sum((i for i in range(a + 1, b) if i not in excluded))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]