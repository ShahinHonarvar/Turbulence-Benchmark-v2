from collections import Counter

def if_contains_anagrams(lst):
    main_list = [i.lower() for i in lst if len(i) >= 3]
    anagram_count = 0
    while main_list:
        word = main_list.pop()
        for index in range(len(main_list)):
            word_dict = dict(Counter(word))
            check_word_dict = dict(Counter(main_list[index]))
            if word_dict == check_word_dict and word != main_list[index]:
                anagram_count += 1
                main_list.pop(index)
                break
    return anagram_count >= 11