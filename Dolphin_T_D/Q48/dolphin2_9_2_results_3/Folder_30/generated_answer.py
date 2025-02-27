def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    missing = [num for num in range(a + 1, b - 1) if num not in numbers]
    if missing:
        sum_missing = sum(missing)
        if sum_missing % 2 == 1:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]
    else:
        return ''