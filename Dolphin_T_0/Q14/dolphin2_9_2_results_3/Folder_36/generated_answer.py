def find_second_smallest_num(numbers):
    sub_list = numbers[209:557]
    if min(sub_list) == max(sub_list):
        return None
    else:
        smallest = min(sub_list)
        second_smallest = max(sub_list)
        for num in sub_list:
            if num < second_smallest and num != smallest:
                second_smallest = num
        if second_smallest == max(sub_list):
            return None
        else:
            return second_smallest