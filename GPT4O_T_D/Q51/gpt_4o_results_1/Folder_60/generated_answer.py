def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    sorted_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    sorted_strings = [s for s in sorted_strings if len(s) >= 3]
    seen_anagrams = set()
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_lower(sorted_strings[i]) == sorted_lower(sorted_strings[j]):
                pair = tuple(sorted([strings[i], strings[j]]))
                if pair not in seen_anagrams:
                    seen_anagrams.add(pair)
                    anagram_count += 1
                    if anagram_count > 77:
                        return False
    return True