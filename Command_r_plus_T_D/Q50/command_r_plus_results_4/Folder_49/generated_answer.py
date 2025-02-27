def if_contains_anagrams(lst: list[str]) -> bool:
    anagram_count = 0
    processed_strings = set()
    for string in lst:
        if len(string) >= 3 and string.lower() not in processed_strings:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_count += sum((1 for s in processed_strings if sorted(s) == sorted_string))
            processed_strings.add(string.lower())
    return anagram_count >= 59