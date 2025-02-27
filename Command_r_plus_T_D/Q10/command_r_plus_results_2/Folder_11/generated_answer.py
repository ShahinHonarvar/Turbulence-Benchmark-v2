def all_odd_ints_exclusive(lst: list[int]) -> list[int]:
    odd_integers = [num for i, num in enumerate(lst[15:99], 15) if num % 2 != 0]
    return odd_integers