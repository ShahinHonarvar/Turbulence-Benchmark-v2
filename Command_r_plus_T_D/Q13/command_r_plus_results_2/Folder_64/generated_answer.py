def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        numbers = sorted(numbers[:5])
        if numbers[3] == numbers[4]:
            return None
        else:
            return numbers[3]