def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 77, len(s) + 1):
            word = s[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    if not palindromes:
        return set()
    return palindromes