def if_contains_anagrams(str_list):
    word_dict = {}
    for word in str_list:
        word = ''.join(sorted([char.lower() for char in word if char.isalpha()]))
        if len(word) >= 3:
            word_dict.setdefault(word, 0)
            word_dict[word] += 1
    if len(word_dict) <= 9:
        return True