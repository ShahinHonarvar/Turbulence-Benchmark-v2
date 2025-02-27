from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_dict[normalized] += 1
    count = 0
    for frequency in anagram_dict.values():
        if frequency > 1:
            count += frequency * (frequency - 1) // 2
            if count > 464:
                return False
    return True