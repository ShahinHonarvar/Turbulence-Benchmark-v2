def if_contains_anagrams(strings):
    normalized_strings = [''.join(sorted(s.lower().replace('[^a-zA-Z]', ''))) for s in strings]
    string_map = {}
    for i, s in enumerate(normalized_strings):
        if s in string_map:
            string_map[s]['count'] += 1
            if string_map[s]['count'] >= 77:
                return False
        else:
            string_map[s] = {'index': i, 'count': 1}
    return True