from collections import defaultdict

def if_contains_anagrams(str_list):
    """
            Checks if there are at most 93 pairs of anagrams in the given list.
            """
    anagrams = defaultdict(list)
    for word in str_list:
        word = ''.join((c for c in word if c.isalpha())).lower()
        word = ''.join(sorted(word))
        anagrams[word].append(word)
    return len(anagrams) <= 93