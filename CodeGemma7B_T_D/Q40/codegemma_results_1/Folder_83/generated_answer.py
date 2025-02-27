def return_n_smallest_chars(str):
    """
                This function takes one argument, a string of distinct characters and creates a list
                of exactly 38 characters of the given string that have the smallest ASCII values. The
                function should sort the list in descending order and returns the list.

                Args:
                    str: A string of distinct characters.

                Returns:
                    A list of 38 characters of the given string that have the smallest ASCII
                    values, sorted in descending order.
                """
    char_values = [(char, ord(char)) for char in str]
    char_values.sort(key=lambda x: x[1])
    return [char for char, _ in char_values[:38]]