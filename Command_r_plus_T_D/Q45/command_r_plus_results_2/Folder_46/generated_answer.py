def palindromes_between_indices(s):
    english_letters = ''.join(filter(str.isalpha, s[4:10].lower()))
    palindromes = set()
    for i in range(len(english_letters) // 2 + 1):
        for j in range(len(english_letters) - 2 * i + 1):
            palindrome = english_letters[j:j + i] + english_letters[j + i:j + 2 * i][::-1]
            if len(palindrome) >= 6:
                palindromes.add(palindrome)
    return palindromes