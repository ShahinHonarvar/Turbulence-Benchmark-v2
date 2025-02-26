def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 66:
        return 0
    filtered_nums = [num for num in numbers[10:67] if num % 2 == 0]
    return sum(filtered_nums)