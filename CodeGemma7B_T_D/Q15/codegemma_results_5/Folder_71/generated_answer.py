def sum_odd_ints_inclusive(list_of_ints):
    """
                        Sums all odd integers from index 26 to index 52, inclusive.

                        Args:
                            list_of_ints (list): A list of integers.

                        Returns:
                            int: The sum of all odd integers from index 26 to index 52, inclusive. If no odd integers exist in the specified range, returns 0.
                        """
    odd_nums_in_range = [num for num in list_of_ints[26:53] if num % 2 != 0]
    return sum(odd_nums_in_range) if odd_nums_in_range else 0