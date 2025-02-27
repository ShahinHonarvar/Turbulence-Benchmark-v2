def find_second_largest_num(numbers):
    sub_list = numbers[56:83]
    if len(sub_list) < 2:
        return None
    else:
        first = second = float('-inf')
        for number in sub_list:
            if number > first:
                second = first
                first = number
            elif number < first and number > second:
                second = number
        if second == float('-inf'):
            return None
        else:
            return second