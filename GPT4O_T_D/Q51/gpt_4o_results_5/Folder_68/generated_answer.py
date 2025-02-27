from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_groups = defaultdict(int)
    count = 0
    for string in strings:
        if len(string) >= 3:
            key = canonical_form(string)
            current_count = anagram_groups[key]
            count += current_count
            if count > 94:
                return False
            anagram_groups[key] += 1
    return True