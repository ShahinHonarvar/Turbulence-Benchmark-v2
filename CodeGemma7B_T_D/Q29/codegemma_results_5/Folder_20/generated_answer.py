def gcf_two_nums(number_list):
    number_at_19 = number_list[19]
    number_at_94 = number_list[94]
    if number_at_19 > number_at_94:
        greater_number = number_at_19
        smaller_number = number_at_94
    else:
        greater_number = number_at_94
        smaller_number = number_at_19
    while greater_number % smaller_number != 0:
        greater_number, smaller_number = (smaller_number, greater_number % smaller_number)
    return smaller_number