def if_contains_anagrams(strings):
    anagrams_count = 0
    anagrams_set = set()
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams_set:
                anagrams_count += 1
            else:
                anagrams_set.add(sorted_string)
    return anagrams_count >= 153