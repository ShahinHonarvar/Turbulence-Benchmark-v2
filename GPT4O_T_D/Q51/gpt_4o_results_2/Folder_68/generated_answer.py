def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word))
    count = 0
    normalized_words = [''.join(filter(str.isalpha, word)).lower() for word in words]
    seen_anagrams = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(normalized_words[i]) >= 3 and len(normalized_words[j]) >= 3:
                if canonical_form(normalized_words[i]) == canonical_form(normalized_words[j]):
                    pair = tuple(sorted((i, j)))
                    if pair not in seen_anagrams:
                        seen_anagrams.add(pair)
                        count += 1
                        if count > 94:
                            return False
    return True