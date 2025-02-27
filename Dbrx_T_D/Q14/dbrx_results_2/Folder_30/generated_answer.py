def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[25:53]) < 2:
        return None
    min_num = min(numbers)
    min_nums = [n for n in numbers[25:53] if n == min_num]
    if len(min_nums) > 1:
        second_min_nums = [n for n in numbers[25:53] if n > min_num]
        if second_min_nums:
            return min(second_min_nums)
        else:
            return None
    else:
        second_min_num = min(set(numbers[25:53]) - set(min_nums))
        return second_min_num