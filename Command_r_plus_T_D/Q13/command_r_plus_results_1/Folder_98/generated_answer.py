def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 7:
        return None
    else:
        numbers = sorted(numbers[:7])
        return numbers[-2]