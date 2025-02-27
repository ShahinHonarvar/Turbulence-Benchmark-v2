def sum_in_range(numbers_list: list[int]) -> int:
    filtered_numbers = [num for num in numbers_list if -358 <= num <= 185]
    return sum(filtered_numbers) if filtered_numbers else 0