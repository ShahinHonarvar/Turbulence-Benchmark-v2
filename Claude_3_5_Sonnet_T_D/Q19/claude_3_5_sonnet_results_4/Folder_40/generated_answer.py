def all_ints_not_div_by_num(integers):
    if len(integers) < 3:
        return []
    start = integers[0] + 1
    end = integers[1]
    divisor = 1
    return [num for num in range(start, end) if num % divisor != 0]