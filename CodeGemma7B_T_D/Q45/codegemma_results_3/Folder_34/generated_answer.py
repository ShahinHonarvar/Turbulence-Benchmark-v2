def palindromes_between_indices(text):
    text = text[5:8].lower()
    set_of_all_palindromes = set()
    for word in set(text):
        if word * 2 in text and word * 3 in text and (word * 4 in text):
            set_of_all_palindromes.add(word * 4)
            set_of_all_palindromes.add(word * 3 + text[text.index(word) + 1])
            set_of_all_palindromes.add(word * 2 + text[text.index(word) + 1:text.index(word, text.index(word) + 2)])
    return set_of_all_palindromes