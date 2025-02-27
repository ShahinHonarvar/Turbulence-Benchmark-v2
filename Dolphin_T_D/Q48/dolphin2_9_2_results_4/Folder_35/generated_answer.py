def return_binary_or_hexa(numbers):
    a, b = (numbers[77], numbers[84])
    sum_not_in_range = sum((number for number in range(a + 1, b) if number not in numbers))
    return bin(sum_not_in_range)[2:] if sum_not_in_range % 2 != 0 else hex(sum_not_in_range)[2:] if sum_not_in_range != 0 else ''