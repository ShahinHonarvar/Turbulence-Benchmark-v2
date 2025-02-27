def if_contains_anagrams(lst):
    count = 0
    processed_words = set()
    for word in lst:
        cleaned_word = ''.join((char for char in word.lower() if char.isalpha()))
        if len(cleaned_word) < 3:
            continue
        sorted_word = ''.join(sorted(cleaned_word))
        if sorted_word in processed_words:
            count += 1
        else:
            processed_words.add(sorted_word)
    return count <= 85