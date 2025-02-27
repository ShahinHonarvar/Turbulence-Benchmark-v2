from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    lower_words = [word.lower() for word in words if len(word) >= 3]
    sorted_map = defaultdict(list)
    for word in lower_words:
        sorted_map[''.join(sorted(word))].append(word)
    anagram_pairs = 0
    for key in sorted_map:
        n = len(sorted_map[key])
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs >= 194:
                return True
    return False