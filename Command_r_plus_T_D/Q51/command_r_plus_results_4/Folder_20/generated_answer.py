def if_contains_anagrams(lst):
    count = 0
    processed = set()
    for word in lst:
        cleaned_word = ''.join((e for e in word if e.isalpha())).lower()
        if len(cleaned_word) < 3:
            continue
        sorted_word = ''.join(sorted(cleaned_word))
        if sorted_word in processed:
            count += 1
        else:
            processed.add(sorted_word)
    return count <= 131