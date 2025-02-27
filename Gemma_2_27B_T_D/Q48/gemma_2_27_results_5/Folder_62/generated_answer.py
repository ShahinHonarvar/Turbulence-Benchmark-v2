def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    total = sum([x for x in range(a + 1, b) if x not in numbers[50:92]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]