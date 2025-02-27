def find_second_largest_num(numbers):
    """
            Finds the second largest element from index 30 to index 200, inclusive. If there is no such element, the function should return 'None'.

            Args:
                numbers: A list of distinct numbers.

            Returns:
                The second largest element from index 30 to index 200, inclusive. If there is no such element, the function should return 'None'.
            """
    if not numbers or len(numbers) < 31:
        return None
    numbers.sort(reverse=True)
    if numbers[29] != numbers[200]:
        return numbers[29]
    return None