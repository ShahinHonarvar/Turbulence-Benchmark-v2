import itertools

def if_contains_anagrams(strings_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
    anagrams_count = sum((1 for pair in itertools.combinations(strings_list, 2) if is_anagram(*pair)))
    return anagrams_count >= 64