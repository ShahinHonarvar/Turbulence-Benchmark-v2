def all_odd_ints_exclusive(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst) if i >= 87 and i < 95 and (num % 2 != 0)]