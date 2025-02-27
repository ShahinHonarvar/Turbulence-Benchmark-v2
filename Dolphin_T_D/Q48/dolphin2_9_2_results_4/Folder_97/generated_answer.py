def return_binary_or_hexa(numbers):
    start = numbers[34]
    end = numbers[69]
    sum_ = sum((n for n in range(start + 1, end + 1) if n not in numbers[34:70]))
    if sum_ == 0:
        return ''
    elif sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()