def if_contains_anagrams(words):
    pairs = 0
    for i in range(len(words) - 1):
        if len(words[i]) > 2 and words[i].lower() not in words[i + 1:]:
            for j in range(i + 1, len(words)):
                if len(words[j]) > 2 and words[i].lower() == words[j].lower():
                    pairs += 1
                    break
    return pairs >= 21