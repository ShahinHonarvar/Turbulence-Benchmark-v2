import collections

def if_contains_anagrams(word_list):
    count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3 and (word_list[i].lower() != word_list[j].lower()) and (collections.Counter(word_list[i].lower()) == collections.Counter(word_list[j].lower())):
                count += 1
                if count >= 21:
                    return True
    return False