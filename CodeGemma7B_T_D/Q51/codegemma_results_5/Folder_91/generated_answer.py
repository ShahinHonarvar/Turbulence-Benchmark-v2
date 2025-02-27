from nltk.corpus import words

def if_contains_anagrams(str_list):

    def is_anagram(str1, str2):
        """
        Checks if two strings are anagrams.

        Args:
            str1: The first string.
            str2: The second string.

        Returns:
            True if the strings are anagrams, False otherwise.
        """
        str1 = str1.lower()
        str2 = str2.lower()
        return sorted(str1) == sorted(str2)
    str_list = [str for str in str_list if str.isalpha() and len(str) >= 3]
    anagrams = {}
    for str in str_list:
        sorted_str = ''.join(sorted(str))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        anagrams[sorted_str].append(str)
    num_pairs = 0
    for anagram_list in anagrams.values():
        num_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return num_pairs <= 88