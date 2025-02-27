def find_second_smallest_num(numbers: list[int]) -> int:
    try:
        second_smallest = sorted(numbers[33:37])[1]
        return second_smallest
    except IndexError:
        return None