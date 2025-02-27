def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 80:
        return None
    min_num = min((num for num in numbers[80:200] if num != float('-inf')))
    second_min_num = min((num for num in numbers[80:200] if num > min_num and num != float('-inf')))
    return second_min_num if second_min_num != float('inf') else None