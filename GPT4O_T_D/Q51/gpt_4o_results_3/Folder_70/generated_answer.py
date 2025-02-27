from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s))
    anagram_counter = defaultdict(int)
    for s in strings:
        cleaned_s = ''.join([char.lower() for char in s if char.isalpha()])
        if len(cleaned_s) >= 3:
            key = sorted_str(cleaned_s)
            anagram_counter[key] += 1
    anagram_pairs = 0
    for count in anagram_counter.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs > 97:
                return False
    return anagram_pairs <= 97