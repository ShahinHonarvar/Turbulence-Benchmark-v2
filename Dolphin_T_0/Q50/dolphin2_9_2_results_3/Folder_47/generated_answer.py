def if_contains_anagrams(words_list):
    count = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3 and (sorted(words_list[i].lower()) == sorted(words_list[j].lower())):
                count += 1
    return count >= 47