def all_ints_div_by_num(numbers):
    divisible_nums = [num for num in numbers[32:36] if num % 91 == 0]
    return divisible_nums if len(divisible_nums) > 0 else []