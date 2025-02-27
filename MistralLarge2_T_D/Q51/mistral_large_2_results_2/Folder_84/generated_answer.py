from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = set()
    counts = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if counts[sorted_str] > 0:
            for existing_string in strings:
                if ''.join(sorted(existing_string.lower())) == sorted_str and (string, existing_string) not in anagram_pairs and ((existing_string, string) not in anagram_pairs):
                    anagram_pairs.add((string, existing_string))
                    if len(anagram_pairs) > 16:
                        return False
        counts[sorted_str] += 1
    return len(anagram_pairs) <= 16