def if_contains_anagrams(str_list):
    seen = set()
    for word in str_list:
        if len(word) < 3:
            continue
        anagram = ''.join(sorted(word.lower()))
        if anagram in seen:
            if len(seen) >= 41:
                return True
        else:
            seen.add(anagram)
    return False