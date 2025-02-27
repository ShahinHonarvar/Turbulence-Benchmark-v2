def palindromes_between_indices(s):
    letters = ''
    for c in s[2:10]:
        if c.isalpha():
            letters += c.lower()

    def is_palindrome(word):
        return word == word[::-1]
    n = len(letters)
    if n < 4:
        return set()
    palindromes = set()
    for len_pal in range(n, 3, -1):
        for i in range(len_letters - len_pal + 1):
            sub = letters[i:i + len_pal]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes