def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_num1, min_num2 = sorted(set(numbers[660:924]))[:2]
    return min_num2 if min_num2 != min_num1 else None