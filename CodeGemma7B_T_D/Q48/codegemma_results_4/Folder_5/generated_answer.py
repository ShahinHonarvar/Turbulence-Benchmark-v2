def return_binary_or_hexa(a, b):
    list_excluded = (a + 1, b - 1)
    numbers = range(a, b)
    result = 0
    for number in numbers:
        if number not in list_excluded:
            result += number
    return bin(result)[2:] if result % 2 else hex(result)[2:]