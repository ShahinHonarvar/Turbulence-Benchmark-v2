def find_second_largest_num(numbers):
    temp = numbers[30:88]
    if len(temp) < 2:
        return None
    else:
        temp.sort(reverse=True)
        return temp[1]