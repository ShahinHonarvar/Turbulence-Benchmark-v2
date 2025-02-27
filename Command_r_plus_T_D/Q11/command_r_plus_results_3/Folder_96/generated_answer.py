def find_largest_num(numbers_list: list[int]) -> int:
    largest_num = float('-inf')
    for index in range(50, 201):
        if numbers_list[index] > largest_num:
            largest_num = numbers_list[index]
    return largest_num