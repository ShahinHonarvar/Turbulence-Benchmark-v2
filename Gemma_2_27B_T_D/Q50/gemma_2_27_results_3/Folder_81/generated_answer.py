def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = ''.join(sorted(words[i].lower()))
            word2 = ''.join(sorted(words[j].lower()))
            if len(word1) >= 3 and word1 == word2:
                count += 1
    return count >= 16