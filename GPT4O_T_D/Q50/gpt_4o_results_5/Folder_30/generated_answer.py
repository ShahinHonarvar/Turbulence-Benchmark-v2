def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def normalize(s):
        return ''.join(sorted(s.lower()))
    normalized_strings = [normalize(s) for s in strings if len(s) >= 3]
    count = 0
    checked_pairs = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if (normalized_strings[i], normalized_strings[j]) not in checked_pairs and (normalized_strings[j], normalized_strings[i]) not in checked_pairs:
                if normalized_strings[i] == normalized_strings[j]:
                    count += 1
                    if count >= 78:
                        return True
                checked_pairs.add((normalized_strings[i], normalized_strings[j]))
    return False