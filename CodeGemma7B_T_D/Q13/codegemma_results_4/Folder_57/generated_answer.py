def find_second_largest_num(numbers: list[int]) -> int:
    """
    This function takes one argument, a list of distinct numbers, as input and returns the second largest element from index 27 to index 55, both inclusive. If there is no such element, the function should return 'None'.
    """
    numbers.sort(reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[27:56][-2]