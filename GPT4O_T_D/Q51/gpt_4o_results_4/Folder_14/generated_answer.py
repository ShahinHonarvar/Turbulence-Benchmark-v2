from collections import defaultdict

def if_contains_anagrams(words):
    words_lowered = [word.lower() for word in words]
    anagram_dict = defaultdict(int)
    pairs_count = 0
    for word in words_lowered:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word] += 1
    for count in anagram_dict.values():
        if count >= 2:
            pairs_count += count * (count - 1) // 2
            if pairs_count > 474:
                return False
    return True