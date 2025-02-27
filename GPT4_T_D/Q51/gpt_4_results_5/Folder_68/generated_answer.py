from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    dict_words = defaultdict(list)
    for curr in lst:
        if len(curr) >= 3:
            sorted_word = ''.join(sorted(curr.lower()))
            if sorted_word in dict_words:
                count += len(dict_words[sorted_word])
                if count > 94:
                    return False
            dict_words[sorted_word].append(curr)
    return True