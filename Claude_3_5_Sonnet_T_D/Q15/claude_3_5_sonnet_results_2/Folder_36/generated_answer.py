def sum_odd_ints_inclusive(int_list):
    start = max(246, 0)
    end = min(751, len(int_list))
    return sum((num for num in int_list[start:end] if num % 2 != 0))