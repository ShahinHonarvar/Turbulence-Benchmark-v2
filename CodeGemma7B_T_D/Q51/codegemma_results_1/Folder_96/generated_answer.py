def if_contains_anagrams(str_list):
    used = set()
    pairs = 0
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word == word.lower():
            continue
        if sorted_word not in used:
            used.add(sorted_word)
        elif sorted_word in used:
            pairs += 1
    if pairs <= 2:
        return True
    else:
        return False