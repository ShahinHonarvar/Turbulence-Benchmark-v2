def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[275:872]]
    total = sum(missing_numbers)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]