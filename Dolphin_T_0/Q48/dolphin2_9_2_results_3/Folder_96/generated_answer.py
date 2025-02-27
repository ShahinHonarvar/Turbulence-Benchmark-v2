def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    missing = [num for num in range(a + 1, b) if num not in numbers[51:200]]
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]