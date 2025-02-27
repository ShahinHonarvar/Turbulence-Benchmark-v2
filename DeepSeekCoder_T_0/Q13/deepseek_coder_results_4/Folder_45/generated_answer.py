def find_second_largest_num(numbers):
    if len(numbers) < 201 or numbers[30:201].count(max(numbers[30:201])) == len(numbers[30:201]):
        return None
    first_max = second_max = float('-inf')
    for num in numbers[30:201]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
    return second_max if second_max != float('-inf') else None