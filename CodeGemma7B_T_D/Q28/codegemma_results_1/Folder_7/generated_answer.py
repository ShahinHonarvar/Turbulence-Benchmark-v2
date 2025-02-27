def return_nth_smallest_ascii(given_string):
    """
            Return the character with the 17th smallest ASCII value among those characters in the string that occur between indices 12 to 55, both inclusive.
            """
    substring = given_string[12:56]
    sorted_substring = sorted(substring)
    return sorted_substring[16]