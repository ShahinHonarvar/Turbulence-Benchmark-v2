from collections import defaultdict

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_dict = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] += 1
    count = 0
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count > 69:
                return False
    return count <= 69