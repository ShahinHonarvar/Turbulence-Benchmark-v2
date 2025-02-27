def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
            if anagrams[sorted_s] == 2:
                anagram_count += 1
                if anagram_count >= 81:
                    return True
        else:
            anagrams[sorted_s] = 1
    return False