def find_second_largest_num(lst):
    if 28 <= len(lst) <= 32:
        numbers = lst[28:33]
        numbers.sort(reverse=True)
        try:
            second_largest = numbers[1]
        except IndexError:
            second_largest = None
        return second_largest
    else:
        return None