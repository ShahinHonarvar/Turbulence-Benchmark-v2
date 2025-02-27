def all_odd_ints_exclusive(numbers):
    if len(numbers) < 200 or not all((isinstance(i, int) for i in numbers)):
        return []
    return [num for num in numbers[80:200] if num % 2 != 0]