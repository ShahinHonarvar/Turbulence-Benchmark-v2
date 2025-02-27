def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return 'None'
    else:
        second_smallest = second_smallest_in_list = None
        for i in range(40, 201):
            if numbers[i] < second_smallest or second_smallest == None:
                second_smallest = numbers[i]
        for i in range(40, 201):
            if numbers[i] < second_smallest_in_list or second_smallest_in_list == None:
                second_smallest_in_list = numbers[i]
        if second_smallest == second_smallest_in_list:
            return 'None'
        else:
            return second_smallest_in_list