from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        cleaned_string = ''.join(sorted(string.lower()))
        if len(cleaned_string) >= 3:
            anagram_dict[cleaned_string] += 1
    count = 0
    for freq in anagram_dict.values():
        count += freq * (freq - 1) // 2
        if count >= 14:
            return True
    return False