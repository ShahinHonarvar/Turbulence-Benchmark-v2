def if_contains_anagrams(lst):
    anagram_count = 0
    processed_strings = set()
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3 and sorted_string not in processed_strings:
            anagram_count += sum((1 for s in processed_strings if sorted(s.lower()) == sorted_string))
            processed_strings.add(sorted_string)
    return anagram_count >= 46