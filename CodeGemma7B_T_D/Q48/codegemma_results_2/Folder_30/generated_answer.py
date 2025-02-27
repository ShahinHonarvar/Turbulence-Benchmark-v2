def return_binary_or_hexa(x):
    if 22 <= len(x) <= 24:
        min_value = x[22] + 1
        max_value = x[24]
        candidates = range(min_value, max_value + 1)
        missing_numbers = [num for num in candidates if num not in x]
        sum = sum(missing_numbers)
        if sum % 2 == 1:
            return '{:b}'.format(sum)
        else:
            return '{:x}'.format(sum)
    else:
        return ''