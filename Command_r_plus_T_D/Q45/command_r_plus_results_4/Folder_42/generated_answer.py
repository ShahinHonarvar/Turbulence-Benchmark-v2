def palindromes_between_indices(s):
    english_letters = ''.join(filter(str.isalpha, s[6:10].lower()))
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes