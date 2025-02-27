def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    second_smallest = None
    smallest = float('inf')
    for num in num_list:
        if num != None:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num != smallest and (second_smallest == None or num < second_smallest):
                second_smallest = num
    return second_smallest