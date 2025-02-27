def if_contains_anagrams(str_list):
    existing_anagrams = {}
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and sorted_word in existing_anagrams:
            existing_anagrams[sorted_word] += 1
            if existing_anagrams[sorted_word] >= 464:
                return False
        else:
            existing_anagrams[sorted_word] = 1
    return True