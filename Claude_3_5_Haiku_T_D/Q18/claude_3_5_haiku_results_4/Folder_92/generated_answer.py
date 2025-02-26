def sum_ints_div_by_either_nums(numbers):
    if not numbers or len(numbers) < 1:
        return 0
    return sum((num for num in numbers[:1] if num % 1 == 0 or num % -1 == 0))