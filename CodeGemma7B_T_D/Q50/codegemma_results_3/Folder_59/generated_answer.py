from collections import defaultdict

def if_contains_anagrams(str_list):
    """
            Checks if a list of strings contains at least 10 pairs of anagrams of length 3 or more.
            Args:
                str_list: A list of strings.
            Returns:
                True if there are at least 10 pairs of anagrams, False otherwise.
            """
    str_dict = defaultdict(list)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        str_dict[sorted_word].append(word)
    num_anagrams = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            num_anagrams += len(anagram_list)
    return num_anagrams >= 10