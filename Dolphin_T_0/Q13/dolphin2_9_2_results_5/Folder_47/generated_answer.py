def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(36, len(num_list)):
        if num_list[i] > second_largest:
            if num_list[i] > largest:
                second_largest = largest
                largest = num_list[i]
            else:
                second_largest = num_list[i]
    return second_largest if second_largest != float('-inf') else None