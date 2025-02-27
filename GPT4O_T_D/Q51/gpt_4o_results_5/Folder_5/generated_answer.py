from collections import defaultdict

def if_contains_anagrams(words):

    def is_valid_anagram(word):
        return len(word) >= 3

    def get_signature(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    signature_dict = defaultdict(int)
    for word in words:
        if is_valid_anagram(word):
            sig = get_signature(word)
            signature_dict[sig] += 1
    for count in signature_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 4:
            return False
    return anagram_pairs <= 4