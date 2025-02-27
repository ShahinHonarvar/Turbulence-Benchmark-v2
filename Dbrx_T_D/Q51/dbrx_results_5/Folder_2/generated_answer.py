import collections

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if collections.Counter(sorted_string) not in (collections.Counter('bcd'), collections.Counter('abc')):
                anagram_count += 1
                if anagram_count > 81:
                    return False
    return True