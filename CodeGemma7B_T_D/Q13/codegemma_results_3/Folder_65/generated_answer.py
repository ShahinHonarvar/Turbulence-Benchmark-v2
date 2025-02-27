def find_second_largest_num(list1):
    larger = largest = min(list1)
    for num in list1[56:99]:
        if num > larger:
            larger = num
            temp = largest
            largest = larger
            larger = temp
        elif num > largest:
            larger = num
    if larger == min(list1):
        return None
    else:
        return larger