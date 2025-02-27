def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    first = max(lst[0], lst[1])
    second = min(lst[0], lst[1])
    for num in lst[2:]:
        if num > first:
            second = first
            first = num
        elif second < num < first:
            second = num
    return second if second != first else None