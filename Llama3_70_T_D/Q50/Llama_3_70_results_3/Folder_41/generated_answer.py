def if_contains_anagrams(strings):
    anagram_count = 0
    sorted_strings = [''.join(sorted(s.casefold())) for s in strings if len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_count += 1
    return anagram_count >= 75