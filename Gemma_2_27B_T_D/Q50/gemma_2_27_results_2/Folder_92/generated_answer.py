def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if sorted(words[i].lower()) == sorted(words[j].lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 2