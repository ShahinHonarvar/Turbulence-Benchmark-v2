def if_contains_anagrams(lst):

    def count_anagrams(lst):
        count = 0
        anagrams_dict = {}
        for word in lst:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                anagrams_dict[sorted_word] = [word]
        for value in anagrams_dict.values():
            if len(value) > 1 and len(value[0]) >= 3:
                count += len(value) * (len(value) - 1) // 2
        return count
    return count_anagrams(lst) >= 54