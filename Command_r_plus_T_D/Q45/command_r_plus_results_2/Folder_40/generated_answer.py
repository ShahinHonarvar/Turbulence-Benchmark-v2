def palindromes_between_indices(s):
    english_letters = ''.join(filter(str.isalpha, s[4:10].lower()))
    palindromes = set()
    for i in range(len(english_letters) - 6):
        for j in range(i + 1, len(english_letters) - (i + 6 - j)):
            palindrome = english_letters[i:j] + english_letters[j:][::-1]
            palindromes.add(palindrome)
    return palindromes