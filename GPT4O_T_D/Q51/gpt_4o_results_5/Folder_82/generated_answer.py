def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings]
    seen = {}
    for i in range(len(normalized_strings)):
        if len(normalized_strings[i]) < 3:
            continue
        for j in range(i + 1, len(normalized_strings)):
            if len(normalized_strings[j]) < 3:
                continue
            if normalized_strings[i] == normalized_strings[j]:
                pair = tuple(sorted((strings[i], strings[j])))
                if pair not in seen:
                    seen[pair] = True
                    anagrams_count += 1
                    if anagrams_count > 40:
                        return False
    return True