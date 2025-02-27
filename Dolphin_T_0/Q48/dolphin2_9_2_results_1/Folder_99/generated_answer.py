def return_binary_or_hexa(numbers):
    if 427 <= 666 < len(numbers):
        a = numbers[427]
        b = numbers[669]
        sum = 0
        for i in range(a + 1, b):
            if i not in numbers:
                sum += i
        if sum % 2:
            return bin(sum)[2:]
        else:
            return hex(sum)[2:]
    return ''