def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    present = numbers[numbers.index(a) + 1:numbers.index(b)]
    if set(range(a + 1, b)) == set(present):
        return ''
    else:
        sum_ = sum(set(range(a + 1, b)) - set(present))
        if sum_ % 2 == 0:
            return hex(sum_)[2:]
        else:
            return bin(sum_)[2:]