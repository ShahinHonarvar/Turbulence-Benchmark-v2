def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            word1 = strings[i].lower()
            word2 = strings[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                if sorted(word1) == sorted(word2):
                    count += 1
    return count <= 10