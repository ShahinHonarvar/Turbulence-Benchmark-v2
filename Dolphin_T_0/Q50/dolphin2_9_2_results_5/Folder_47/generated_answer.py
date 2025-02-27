def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            for others in lst:
                if word.lower() != others.lower() and len(others) >= 3 and (sorted_word == ''.join(sorted(others.lower()))):
                    count += 1
    return count >= 47