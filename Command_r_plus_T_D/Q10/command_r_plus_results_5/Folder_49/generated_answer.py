def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [num for i, num in enumerate(int_list) if num % 2 != 0 and 80 <= i < 200]
    return odd_ints