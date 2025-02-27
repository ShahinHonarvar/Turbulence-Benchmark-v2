def find_second_largest_num(numbers):
    if len(numbers) < 201 or numbers[40:201].count(max(numbers[40:201])) == len(numbers[40:201]):
        return None
    first_max = max(numbers[40:201])
    second_max = float('-inf')
    for num in numbers[40:201]:
        if num != first_max and num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None