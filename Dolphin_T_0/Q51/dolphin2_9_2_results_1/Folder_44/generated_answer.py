def if_contains_anagrams(lst):
    count = 0
    dictionary = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and len(sorted_word) > 1 and (sorted_word not in dictionary):
            dictionary[sorted_word] = 1
            hits = sum((v for k, v in dictionary.items() if k == sorted_word))
            count += hits
    return count <= 75