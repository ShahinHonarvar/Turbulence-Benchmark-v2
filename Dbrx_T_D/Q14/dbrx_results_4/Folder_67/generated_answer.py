def find_second_smallest_num(numbers):
    if len(numbers) < 55 or min(numbers[50:55]) == max(numbers[50:55]):
        return None
    sorted_numbers = sorted(numbers[50:55])
    second_smallest = sorted_numbers[1]
    return second_smallest