def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    subset = numbers[43:70]
    missing_numbers = [i for i in range(a + 1, b) if i not in subset]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return x.to_bytes((x.bit_length() + 7) // 8, 'big').hex()
    else:
        return bin(sum_missing)[2:]