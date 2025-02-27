def if_contains_anagrams(lst_of_words):
    count = 0
    for i in range(len(lst_of_words)):
        for j in range(i + 1, len(lst_of_words)):
            if len(lst_of_words[i]) >= 3 and len(lst_of_words[j]) >= 3:
                if sorted(lst_of_words[i].lower()) == sorted(lst_of_words[j].lower()):
                    count += 1
    return count >= 61