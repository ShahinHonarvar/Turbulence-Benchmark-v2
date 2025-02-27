from collections import defaultdict

def if_contains_anagrams(strings):

    def signature(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    sig_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sig = signature(s)
            anagram_count += sig_dict[sig]
            sig_dict[sig] += 1
    return anagram_count >= 219