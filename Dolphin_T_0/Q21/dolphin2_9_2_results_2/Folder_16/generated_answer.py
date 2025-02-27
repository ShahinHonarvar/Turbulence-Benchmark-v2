def all_ints_div_by_num(numbers):
    divisible = [num for num in numbers[12:69] if num % 71 == 0]
    if not divisible:
        divisible = []
    return divisible