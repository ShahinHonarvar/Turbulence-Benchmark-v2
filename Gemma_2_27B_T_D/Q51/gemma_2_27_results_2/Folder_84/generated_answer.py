def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            w1 = words[i].lower()
            w2 = words[j].lower()
            if len(w1) >= 3 and len(w2) >= 3 and (sorted(w1) == sorted(w2)) and (w1 != w2):
                count += 1
    return count <= 16