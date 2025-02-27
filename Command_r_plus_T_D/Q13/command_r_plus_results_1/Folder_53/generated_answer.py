def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(100, 201):
        if num_list[i] > largest:
            second_largest = largest
            largest = num_list[i]
        elif largest > num_list[i] > second_largest:
            second_largest = num_list[i]
    return second_largest if second_largest != float('-inf') else None