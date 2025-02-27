def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                word1 = words[i].lower()
                word2 = words[j].lower()
                if sorted(word1) == sorted(word2):
                    count += 1
    return count <= 147