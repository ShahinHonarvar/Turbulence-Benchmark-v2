from collections import Counter

def if_contains_anagrams(the_list):
    the_list = [word.lower() for word in the_list if len(word) >= 3]
    for i in range(len(the_list)):
        for j in range(i + 1, len(the_list)):
            if Counter(the_list[i]) == Counter(the_list[j]):
                return True
    return False