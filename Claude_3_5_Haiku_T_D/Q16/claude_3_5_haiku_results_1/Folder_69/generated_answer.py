def sum_even_ints_inclusive(numbers):
    if len(numbers) < 36:
        return 0
    even_nums = [num for num in numbers[32:36] if num % 2 == 0]
    return sum(even_nums) if even_nums else 0