def if_contains_anagrams(strings):
    anagrams = {}
    anagram_count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagram_count += 1
            if anagram_count > 257:
                return False
        else:
            anagrams[sorted_str] = True
    return True