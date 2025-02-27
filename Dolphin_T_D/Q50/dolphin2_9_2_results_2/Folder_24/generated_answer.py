def if_contains_anagrams(lst):
    anagrams = 0
    for words in zip(lst, lst[1:]):
        if words[0].lower() != words[1].lower():
            if sorted(words[0].lower()) == sorted(words[1].lower()) and len(words[0]) >= 3 and (len(words[1]) >= 3):
                anagrams += 1
    if anagrams >= 65:
        return True
    else:
        return False