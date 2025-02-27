def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 56):
        word = s[i:i + 57]
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes