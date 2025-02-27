def if_contains_anagrams(lst):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    anagrams_count = 0
    anagrams = []
    length = len(lst)
    for i in range(length):
        if len(lst[i]) >= 3:
            anagrams.append(lst[i].lower())
            for j in range(i + 1, length):
                if len(lst[j]) >= 3 and sorted(lst[j].lower()) in anagrams:
                    anagrams_count += 1
                    break
                else:
                    anagrams.append(lst[j].lower())
    return anagrams_count <= 18