def if_contains_anagrams(lst):
    seen_anagrams = set()
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in seen_anagrams:
            return False
        seen_anagrams.add(sorted_string)
    return True