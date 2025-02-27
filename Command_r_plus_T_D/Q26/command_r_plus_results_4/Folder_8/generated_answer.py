def sum_in_range(numbers_list):
    filtered_numbers = [num for num in numbers_list if -33 <= num <= 93]
    return sum(filtered_numbers) if filtered_numbers else 0