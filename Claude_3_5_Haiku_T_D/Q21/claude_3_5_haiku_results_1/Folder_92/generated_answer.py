def all_ints_div_by_num(numbers):
    if not numbers:
        return []
    divisible_nums = [num for num in numbers[:1] if num % 1 == 0]
    return divisible_nums