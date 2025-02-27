def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    if all((i in numbers for i in range(a, b))):
        return ''
    else:
        sum = 0
        for i in range(a + 1, b):
            if i not in numbers:
                sum += i
        if sum % 2 == 0:
            return hex(sum)[2:]
        else:
            return bin(sum)[2:]