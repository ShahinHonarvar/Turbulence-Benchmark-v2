def find_second_largest_num(num_list):
    if len(num_list) < 527:
        return 'None'
    num_list.sort(reverse=True)
    return num_list[526] if num_list[526] != num_list[527] else 'None'