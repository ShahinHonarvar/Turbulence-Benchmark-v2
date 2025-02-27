def if_contains_anagrams(strings):

    def to_sorted_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_chars = to_sorted_chars(string)
        if sorted_chars in anagrams:
            pair_count = anagrams[sorted_chars]
            count += pair_count
            if count >= 26:
                return True
            anagrams[sorted_chars] = pair_count + 1
        else:
            anagrams[sorted_chars] = 1
    return False