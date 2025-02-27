from string import ascii_lowercase

def palindromes_of_specific_lengths(word):
    letters = ascii_lowercase
    res = set()
    for left in letters:
        for right in letters:
            for length in range(3, 11):
                start, end = (letters.index(left), len(letters) - letters[::-1].index(right) - 1)
                if start + length <= end and word[start:start + length] in letters * length:
                    res.add(word[start:start + length])
    return res