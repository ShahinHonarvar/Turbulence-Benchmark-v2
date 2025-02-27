def find_second_smallest_num(num_list):
    num_list = num_list[62:79]
    if len(num_list) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in num_list:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None