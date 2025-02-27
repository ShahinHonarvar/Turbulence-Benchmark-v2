def find_second_smallest_num(numbers):
    try:
        num_len = len(numbers)
        if num_len >= 65:
            numbers.sort()
            return numbers[64:67][1]
        else:
            return None
    except:
        return None