def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    else:
        start = 22
        end = 50
        sub_list = numbers[start:end + 1]
        if len(sub_list) == 29:
            unique_sub_list = set(sub_list)
            if len(unique_sub_list) == 29:
                sorted_sub_list = sorted(unique_sub_list)
                return sorted_sub_list[1]
            else:
                return None
        else:
            return None