def if_contains_anagrams(word_list):
    anagrams = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if sorted(word_list[i].lower()) == sorted(word_list[j].lower()) and len(word_list[i]) >= 3 and (len(word_list[j]) >= 3):
                anagrams += 1
                if anagrams >= 9:
                    return True
    return False