def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            a = sorted(words[i].lower())
            b = sorted(words[j].lower())
            if a == b and len(words[i]) >= 3:
                count += 1
    return count >= 84