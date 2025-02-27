def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string in strings:
        if len(string) >= 3:
            anagram = ''.join(sorted(string.lower()))
            for other_string in strings:
                if string != other_string and len(other_string) >= 3:
                    if anagram == ''.join(sorted(other_string.lower())):
                        anagram_pairs += 1
    return anagram_pairs >= 42