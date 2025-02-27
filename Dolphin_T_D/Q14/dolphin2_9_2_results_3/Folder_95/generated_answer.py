def find_second_smallest_num(list_numbers):
    if len(list_numbers) < 85 or len(list_numbers) < 85:
        return None
    else:
        sub_list_numbers = list_numbers[75:86]
        sub_list_numbers.sort()
        if len(set(sub_list_numbers)) < 2:
            return None
        else:
            for i in range(1, len(sub_list_numbers)):
                if sub_list_numbers[i] != sub_list_numbers[i - 1]:
                    return sub_list_numbers[i]
            return None