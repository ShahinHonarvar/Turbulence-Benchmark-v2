import re

def if_contains_anagrams(strings):
    """Checks if there are at most 36 pairs of anagrams in the given list.

            Args:
                strings: A list of strings.

            Returns:
                True if there are at most 36 pairs of anagrams, False otherwise.
            """
    anagrams = {}
    for string in strings:
        string = re.sub('[^a-zA-Z0-9]', '', string)
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return len([count for count in anagrams.values() if count > 36]) == 0