def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    missing = [i for i in range(a + 1, b) if i not in numbers]
    sum = 0 if not missing else sum(missing)
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]