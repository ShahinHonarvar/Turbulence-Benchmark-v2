def palindrome_of_length_at_least_n(s):
    s = ''.join((c.upper() if c.isalpha() else ' ' for c in s)).split()
    palindromes = set()
    for word in s:
        if len(word) >= 40 and word == word[::-1]:
            palindromes.add(word)
    return palindromes