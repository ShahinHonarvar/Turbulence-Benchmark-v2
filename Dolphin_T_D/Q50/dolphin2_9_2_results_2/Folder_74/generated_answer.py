def if_contains_anagrams(words):
    count = 0
    for i in range(len(words) - 1):
        if len(words[i]) >= 3:
            for j in range(i + 1, len(words)):
                if sorted(words[i].lower()) == sorted(words[j].lower()):
                    count += 1
                    if count >= 17:
                        return True
    return False