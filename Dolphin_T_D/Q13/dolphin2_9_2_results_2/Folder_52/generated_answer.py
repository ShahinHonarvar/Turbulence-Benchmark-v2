def find_second_largest_num(numbers):
    if 38 < len(numbers) < 28:
        return None
    else:
        subsection = numbers[28:39]
        if len(subsection) < 2:
            return None
        else:
            max_num = max(subsection)
            subsection.remove(max_num)
            if len(subsection) < 2:
                return None
            else:
                second_max_num = max(subsection)
                return second_max_num