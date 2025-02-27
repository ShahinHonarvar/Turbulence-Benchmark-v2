from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    checked = set()
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        for checked_string in checked:
            if is_anagram(sorted_string, checked_string):
                anagram_count += 1
                if anagram_count > 92:
                    return False
        checked.add(sorted_string)
    return True