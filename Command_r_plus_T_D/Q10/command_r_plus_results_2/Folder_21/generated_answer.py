def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_integers = [num for num in numbers_list[743:867] if num % 2 != 0]
    return odd_integers