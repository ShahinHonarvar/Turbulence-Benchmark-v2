from collections import defaultdict

def if_contains_anagrams(strings):

    def is_valid_anagram_pair(word1, word2):
        return sorted(word1) == sorted(word2) and len(word1) >= 3
    normalized_strings = [s.lower() for s in strings]
    anagram_count = 0
    seen_pairs = defaultdict(bool)
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if is_valid_anagram_pair(normalized_strings[i], normalized_strings[j]):
                pair = tuple(sorted([normalized_strings[i], normalized_strings[j]]))
                if not seen_pairs[pair]:
                    anagram_count += 1
                    seen_pairs[pair] = True
                if anagram_count > 66:
                    return False
    return True