def find_second_smallest_num(numbers):
    num_list = numbers[82:87]
    if len(num_list) < 2:
        return None
    first_smallest = num_list[0]
    second_smallest = float('inf')
    for num in num_list:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest