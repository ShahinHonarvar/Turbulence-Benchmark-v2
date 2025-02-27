def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s))
    normalized_strings = [sort_string(s.lower()) for s in strings if len(s) >= 3]
    count = 0
    seen_pairs = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                pair = tuple(sorted((strings[i].lower(), strings[j].lower())))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    count += 1
                    if count > 5:
                        return False
    return True