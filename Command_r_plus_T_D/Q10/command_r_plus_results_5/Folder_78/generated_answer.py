def all_odd_ints_exclusive(lst: list[int]) -> list[int]:
    odd_ints = [num for i, num in enumerate(lst) if num % 2 != 0 and 20 <= i < 35]
    return odd_ints