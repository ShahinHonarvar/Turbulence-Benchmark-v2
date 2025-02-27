from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = sorted_chars(string)
            anagrams[key] += 1
    count = 0
    for count_of_string in anagrams.values():
        if count_of_string > 1:
            count += count_of_string * (count_of_string - 1) // 2
        if count >= 28:
            return True
    return False