def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[97]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[10:98]:
            missing_numbers.append(i)
    if missing_numbers:
        total = sum(missing_numbers)
        if total % 2 == 0:
            return hex(total)[2:]
        else:
            return bin(total)[2:]
    else:
        return ''