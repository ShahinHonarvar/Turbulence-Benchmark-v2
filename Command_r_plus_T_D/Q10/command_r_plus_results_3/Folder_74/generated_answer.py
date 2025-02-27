def all_odd_ints_exclusive(lst: list[int]) -> list[int]:
    odd_ints = [lst[i] for i in range(13, 70) if lst[i] % 2 != 0]
    return odd_ints