def if_contains_anagrams(words):
    counter = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if sorted(words[i].lower()) == sorted(words[j].lower()):
                    counter += 1
    if counter >= 95:
        return True
    else:
        return False