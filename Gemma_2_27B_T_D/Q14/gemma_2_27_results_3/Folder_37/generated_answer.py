def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[5:8])[1]
    except:
        return None