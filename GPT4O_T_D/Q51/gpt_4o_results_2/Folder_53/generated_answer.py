from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        canonical = canonical_form(''.join(filter(str.isalpha, string)))
        seen[canonical] += 1
    for count in seen.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count > 8:
                return False
    return True