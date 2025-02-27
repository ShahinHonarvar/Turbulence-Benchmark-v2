def sum_ints_div_by_either_nums(num_list):
    relevant_numbers = num_list[200:201]
    sum_of_numbers = 0
    for number in relevant_numbers:
        if number % 17 == 0 or number % -5 == 0:
            sum_of_numbers += number
    if sum_of_numbers == 0:
        return 0
    else:
        return sum_of_numbers