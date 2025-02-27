def return_n_greatest_chars(character_string):
    """
            Write a function called 'return_n_greatest_chars' that takes one argument, a string of distinct characters and creates the sorted list of exactly 59 characters of the given string that have the greatest ASCII values. The function should sort the list in descending order and returns it.
            """

    def get_ascii_value(character):
        """
                Returns the ASCII value of a given character.
                """
        return ord(character)

    def compare_ascii_values(char1, char2):
        """
                Compares the ASCII values of two characters and returns the appropriate boolean value.
                """
        return get_ascii_value(char1) > get_ascii_value(char2)
    characters = list(character_string)
    characters.sort(key=get_ascii_value, reverse=True)
    return characters[:59]