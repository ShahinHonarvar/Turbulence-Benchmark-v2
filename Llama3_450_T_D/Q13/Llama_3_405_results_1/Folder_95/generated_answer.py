def find_second_largest_num(num_list):
    try:
        numbers = num_list[82:87]
        numbers.sort(reverse=True)
        return numbers[1]
    except IndexError:
        return None