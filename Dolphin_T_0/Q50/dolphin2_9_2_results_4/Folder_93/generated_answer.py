from collections import Counter

def if_contains_anagrams(word_list):
    count = 0
    for i in range(len(word_list)):
        if len(word_list[i]) >= 3:
            word_sort = ''.join(sorted(word_list[i].lower()))
            for j in range(i + 1, len(word_list)):
                if len(word_list[j]) >= 3:
                    if ''.join(sorted(word_list[j].lower())) == word_sort:
                        count += 1
    return count >= 18