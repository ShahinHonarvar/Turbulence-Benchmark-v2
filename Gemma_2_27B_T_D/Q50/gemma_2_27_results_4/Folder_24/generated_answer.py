def if_contains_anagrams(words):
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if sorted(words[i].lower()) == sorted(words[j].lower()):
                    count += 1
    return count >= 65