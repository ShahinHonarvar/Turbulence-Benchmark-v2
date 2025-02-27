def palindromes_between_indices(s):
    letters = s[4:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindrome_set = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 6 and set(substring) <= english_letters and (substring == substring[::-1]):
                palindrome_set.add(substring)
    return palindrome_set