def if_contains_anagrams(strings):
    anagram_pairs = 0
    string_length = len(strings)
    checked_pairs = 0
    for i in range(string_length):
        for j in range(i + 1, string_length):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_pairs += 1
            checked_pairs += 1
    return anagram_pairs <= 21