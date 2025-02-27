def if_contains_anagrams(data):
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            word1 = data[i].lower()
            word2 = data[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                if sorted(word1) == sorted(word2):
                    count += 1
    return count <= 257