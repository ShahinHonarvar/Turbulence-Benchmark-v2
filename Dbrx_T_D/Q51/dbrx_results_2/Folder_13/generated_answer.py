import re

def if_contains_anagrams(words: list[str]) -> bool:
    anagrams = set()
    word_set = set()
    for word in words:
        sorted_word = ''.join(sorted(re.findall('\\b\\w+\\b', word.lower())))
        if len(sorted_word) >= 3:
            if sorted_word in word_set:
                anagrams.add(sorted_word)
                if len(anagrams) > 54:
                    return False
            else:
                word_set.add(sorted_word)
    return True