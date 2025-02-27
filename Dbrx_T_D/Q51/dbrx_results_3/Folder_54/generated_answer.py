import collections

def if_contains_anagrams(strings_list):
    anagram_count = 0
    for string in strings_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if collections.Counter(sorted_string) not in (collections.Counter('a' * len(sorted_string)), collections.Counter('b' * len(sorted_string))):
                anagram_count += 1
                if anagram_count > 39:
                    return False
    return True