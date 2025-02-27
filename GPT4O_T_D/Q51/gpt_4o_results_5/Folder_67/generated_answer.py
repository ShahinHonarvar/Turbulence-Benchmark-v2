def if_contains_anagrams(words):
    word_pairs = set()
    normalized_strings = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j]:
                word_pairs.add((min(words[i].lower(), words[j].lower()), max(words[i].lower(), words[j].lower())))
                if len(word_pairs) > 5:
                    return False
    return True