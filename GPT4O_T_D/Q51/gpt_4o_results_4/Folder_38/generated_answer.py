from collections import defaultdict

def if_contains_anagrams(strings):

    def hash_word(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            hashed = hash_word(string)
            anagram_dict[hashed] += 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 416