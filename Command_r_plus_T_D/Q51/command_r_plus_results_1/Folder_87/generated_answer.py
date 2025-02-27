def if_contains_anagrams(lst):
    count = 0
    words = [word.lower() for word in lst]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (sorted(words[i]) == sorted(words[j])):
                count += 1
                if count > 392:
                    return False
    return True