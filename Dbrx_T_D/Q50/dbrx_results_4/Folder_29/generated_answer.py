import itertools

def if_contains_anagrams(strings_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower()) and len(str1) >= 3 and (str1 != str2)
    return sum((is_anagram(str1, str2) for str1, str2 in itertools.combinations(strings_list, 2))) >= 35