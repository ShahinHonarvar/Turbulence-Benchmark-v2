def find_second_smallest_num(numbers):
    try:
        chunk = sorted(numbers[74:96])
        return chunk[1]
    except IndexError:
        return None