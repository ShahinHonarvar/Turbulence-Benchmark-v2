def return_binary_or_hexa(numbers):
    a, b = (numbers[36], numbers[54])
    sub_list = [num for num in numbers[36:55] if num > a and num < b]
    missing_numbers = set(range(a + 1, b)) - set(sub_list)
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]