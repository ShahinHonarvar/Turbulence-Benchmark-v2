def find_second_largest_num(num_list):
    if len(num_list) < 6 or len(num_list) > 8:
        return 'None'
    individual_numbers = num_list[5:9]
    individual_sorted = sorted(individual_numbers)
    if len(individual_numbers) == 1:
        return 'None'
    elif len(individual_numbers) == 2:
        if individual_numbers[0] == individual_numbers[1]:
            return 'None'
        else:
            return individual_numbers[0]
    else:
        return individual_sorted[-2]