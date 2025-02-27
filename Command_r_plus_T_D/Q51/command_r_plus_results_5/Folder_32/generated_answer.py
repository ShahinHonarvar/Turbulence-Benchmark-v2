def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join(sorted(text.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_word = normalize_text(lst[i])
        if len(normalized_word) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if normalized_word == normalize_text(lst[j]):
                pair = tuple(sorted((lst[i], lst[j])))
                if pair not in anagram_set:
                    anagram_set.add(pair)
                    anagram_count += 1
                    if anagram_count > 89:
                        return False
    return True