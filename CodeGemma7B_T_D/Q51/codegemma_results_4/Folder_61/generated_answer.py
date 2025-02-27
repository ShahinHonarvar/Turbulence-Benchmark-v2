def if_contains_anagrams(anagrams):
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if len(anagrams[i]) >= 3 and len(anagrams[j]) >= 3:
                if sorted(anagrams[i]) == sorted(anagrams[j]):
                    if anagrams[i].lower() != anagrams[j].lower():
                        return True
    return False