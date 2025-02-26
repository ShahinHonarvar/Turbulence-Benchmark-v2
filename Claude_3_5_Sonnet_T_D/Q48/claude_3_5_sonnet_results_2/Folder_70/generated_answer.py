def return_binary_or_hexa(tuple_input):
    a = tuple_input[43]
    b = tuple_input[70]
    all_numbers = set(range(a + 1, b))
    tuple_numbers = set(tuple_input[43:71])
    missing_numbers = all_numbers - tuple_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]