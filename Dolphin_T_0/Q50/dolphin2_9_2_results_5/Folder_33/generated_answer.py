def if_contains_anagrams(lst):
    count = 0
    checked = set()
    for word in lst:
        if len(word) < 3 or not word.isalpha():
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in checked:
            count += 1
        else:
            checked.add(sorted_word)
    return count >= 140