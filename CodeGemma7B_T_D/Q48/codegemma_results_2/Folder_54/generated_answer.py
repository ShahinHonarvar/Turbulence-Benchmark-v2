def return_binary_or_hexa(numbers):
    sum_ = 0
    for i in range(numbers[35] + 1, numbers[64]):
        if i not in numbers[35:65]:
            sum_ += i
    if sum_ & 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper() if sum_.bit_length() <= 28 else hex(sum_)[2:].lower()