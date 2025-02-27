def palindromes_between_indices(s):
    palindrome_set = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(4, 9):
        for j in range(i, 9):
            substring = s[i:j + 1].lower()
            if len(substring) >= 6 and set(substring) <= set(english_letters):
                if substring == substring[::-1]:
                    palindrome_set.add(substring)
    return palindrome_set