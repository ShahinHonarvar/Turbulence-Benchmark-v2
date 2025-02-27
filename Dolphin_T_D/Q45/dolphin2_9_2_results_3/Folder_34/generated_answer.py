def palindromes_between_indices(string):
    substring = string[5:8]
    letters = set()
    for letter in substring.lower():
        if letter.isalpha():
            letters.add(letter)
    palindromes = set()
    if len(letters) >= 2:
        for a in letters:
            for b in letters:
                if a == b or (a < b and a != 'e' and (b != '3')):
                    for c in letters:
                        for d in letters:
                            if c == d or (c < d and c != 'e' and (d != '3')):
                                word = a + b + c + d
                                if word == word[::-1]:
                                    palindromes.add(word)
    return palindromes