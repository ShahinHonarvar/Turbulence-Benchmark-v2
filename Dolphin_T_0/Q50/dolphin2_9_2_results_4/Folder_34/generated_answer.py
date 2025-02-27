def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                words[i] = words[i].lower()
                words[j] = words[j].lower()
                if sorted(words[i]) == sorted(words[j]):
                    count += 1
    return count >= 25