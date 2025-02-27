def if_contains_anagrams(str_list):
    words = {''.join(sorted(word.lower())): word for word in str_list if len(word) >= 3}
    pairs = 0
    for first, second in itertools.combinations(words.values(), 2):
        pairs += 1
        if first == second:
            continue
        if sorted(first) == sorted(second):
            return False
    return pairs <= 39