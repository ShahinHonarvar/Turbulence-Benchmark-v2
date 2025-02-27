def if_contains_anagrams(text):
    """ checks if list of strings contains at least 55 pairs of anagrams """
    count = 0
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if sorted(text[i].lower()) == sorted(text[j].lower()):
                if len(text[i]) >= 3 and len(text[j]) >= 3:
                    count += 1
    return count >= 55