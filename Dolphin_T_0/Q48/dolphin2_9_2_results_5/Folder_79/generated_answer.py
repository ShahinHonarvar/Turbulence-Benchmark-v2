def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[7]
    total = 0
    present_numbers = [num for num in numbers[1:7]]
    for i in range(a + 1, b):
        if i not in present_numbers:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()