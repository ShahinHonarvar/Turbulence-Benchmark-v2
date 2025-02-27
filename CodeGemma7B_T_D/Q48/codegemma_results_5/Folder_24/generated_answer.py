def return_binary_or_hexa(numbers):
    sum_missing = 0
    for i in range(numbers[14] + 1, numbers[92]):
        if i not in numbers[13:92]:
            sum_missing += i
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()