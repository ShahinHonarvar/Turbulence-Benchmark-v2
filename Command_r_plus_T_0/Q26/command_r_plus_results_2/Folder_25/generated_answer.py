def sum_in_range(numbers_list):
    filtered_numbers = [num for num in numbers_list if -10 <= num <= 48]
    return sum(filtered_numbers) if filtered_numbers else 0