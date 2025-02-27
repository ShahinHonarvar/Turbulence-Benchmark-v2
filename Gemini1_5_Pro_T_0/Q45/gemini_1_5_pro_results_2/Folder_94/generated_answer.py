def palindromes_between_indices(string):
    letters = set()
    for i in range(3, 5):
        if string[i].isalpha():
            letters.add(string[i].lower())
    result = set()
    for letter1 in letters:
        for letter2 in letters:
            result.add(letter1 + letter2 + letter1)
            result.add(letter2 + letter1 + letter2)
    return result