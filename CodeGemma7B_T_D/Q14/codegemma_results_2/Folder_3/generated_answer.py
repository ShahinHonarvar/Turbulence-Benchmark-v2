def find_second_smallest_num(numbers):
    """
            finds the second smallest element from index 27 to index 55, both inclusive.
            If there is no such an element, the function should return 'None'.
            """
    numbers.sort()
    if len(numbers) <= 53:
        return None
    return numbers[27]