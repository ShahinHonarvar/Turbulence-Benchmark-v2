def all_ints_div_by_num(numbers, start, end):
    if start > end or start < 0 or end > len(numbers):
        return []
    else:
        result = [numbers[i] for i in range(start, end + 1) if numbers[i] % 9 == 0]
        return result