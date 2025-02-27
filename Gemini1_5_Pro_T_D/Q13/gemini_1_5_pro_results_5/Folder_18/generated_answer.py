def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return 'None'
    else:
        sliced_list = numbers[35:50]
        sliced_list.sort()
        if len(sliced_list) == 1:
            return 'None'
        else:
            return sliced_list[-2]