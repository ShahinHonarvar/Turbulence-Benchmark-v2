def if_contains_anagrams(words):
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if sorted(words[i].lower()) == sorted(words[j].lower()):
                    anagram_count += 1
                    if anagram_count >= 10:
                        return True
    return False