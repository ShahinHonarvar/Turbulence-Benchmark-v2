from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if len(s) >= 3]
    signature_map = defaultdict(list)
    for string in valid_strings:
        signature = sort_string(string)
        signature_map[signature].append(string)
    anagram_pairs = 0
    for signature, words in signature_map.items():
        n = len(words)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 19:
            return False
    return True