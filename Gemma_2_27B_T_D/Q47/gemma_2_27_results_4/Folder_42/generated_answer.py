from string import ascii_letters

def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[43:96]
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            word = substring[i:j + 1]
            if len(word) in range(18, 48) and all((char in ascii_letters for char in word)) and (word.lower() == word[::-1].lower()):
                palindromes.add(word)
    return palindromes