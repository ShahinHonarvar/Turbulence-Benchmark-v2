def palindromes_of_specific_lengths(text):
    ret = set()
    if len(text) < 15 or len(text) > 94:
        return ret
    text = text[14:95].lower()
    for word in text.split():
        if not word.isalpha():
            continue
        if len(word) < 18 or len(word) > 73:
            continue
        if word == word[::-1]:
            ret.add(word)
    return ret