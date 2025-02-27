def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[50:93]:
            total += num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]