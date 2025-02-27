def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[3]
    sum_of_missing = 0
    for i in range(a + 1, b):
        if i not in numbers[0:4]:
            sum_of_missing += i
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].lower()