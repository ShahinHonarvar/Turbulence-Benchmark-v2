def if_contains_anagrams(s):
    count, check = (0, {})
    for word in s:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            if word_sorted in check:
                count += 1
                if count >= 106:
                    return True
            else:
                check[word_sorted] = True
    return False