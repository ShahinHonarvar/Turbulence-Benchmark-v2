def if_contains_anagrams(strings):

    def normalize_str(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    normalized_strings = [normalize_str(s) for s in strings if len(s) >= 3]
    checked_strings = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                pair = (min(strings[i].lower(), strings[j].lower()), max(strings[i].lower(), strings[j].lower()))
                if pair not in checked_strings:
                    anagram_pairs += 1
                    checked_strings.add(pair)
                    if anagram_pairs > 4:
                        return False
    return True