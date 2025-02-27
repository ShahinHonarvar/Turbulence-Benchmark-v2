def find_n_th_smallest_num(numbers):
    relevant_numbers = numbers[34:95]
    relevant_numbers.sort()
    if len(relevant_numbers) < 18:
        return 'Error: Not enough numbers in the relevant slice'
    else:
        return relevant_numbers[17]