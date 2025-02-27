def find_second_largest_num(numbers):
    sublist = numbers[40:81]
    if len(sublist) < 2:
        return None
    else:
        largest = sublist[0]
        second_largest = None
        for num in sublist:
            if num > largest:
                second_largest = largest
                largest = num
            elif second_largest is None or second_largest < num < largest:
                second_largest = num
        return second_largest