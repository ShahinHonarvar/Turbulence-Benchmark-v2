def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_chars(strings[i]) == sorted_chars(strings[j]):
                    pair = tuple(sorted((strings[i].lower(), strings[j].lower())))
                    if pair not in seen:
                        seen.add(pair)
                        anagram_count += 1
                        if anagram_count > 47:
                            return False
    return True