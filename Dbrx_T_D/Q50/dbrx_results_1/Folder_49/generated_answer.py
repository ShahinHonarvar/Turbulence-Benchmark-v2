import itertools

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            for other_word in itertools.islice(string_list[string_list.index(word) + 1:], 0, None):
                if len(other_word) >= 3 and sorted_word == ''.join(sorted(other_word.lower())) and (word.lower() != other_word.lower()):
                    anagrams_count += 1
                    if anagrams_count >= 59:
                        return True
    return False