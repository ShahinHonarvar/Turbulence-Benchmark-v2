def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    count = 0
    for i in range(0, len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (sorted(words[i]) == sorted(words[j])):
                count += 1
    return count <= 55