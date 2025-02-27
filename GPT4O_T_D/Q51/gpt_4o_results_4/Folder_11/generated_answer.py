from collections import defaultdict

def if_contains_anagrams(strings):
    normalized_dict = defaultdict(int)
    for word in strings:
        normalized_word = ''.join(sorted(word.lower()))
        if len(normalized_word) >= 3:
            normalized_dict[normalized_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in normalized_dict.values() if count > 1))
    return anagram_pairs <= 41