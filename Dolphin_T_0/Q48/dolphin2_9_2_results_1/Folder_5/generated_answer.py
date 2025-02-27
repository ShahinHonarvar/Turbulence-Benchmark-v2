def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    total = suml(range(a + 1, b)) - sum(numbers[3:9])
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]