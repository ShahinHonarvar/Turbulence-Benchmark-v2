def palindrome_of_length_at_least_n(s):
    n = 149
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            word = s[i:j + 1]
            if word == word[::-1] and len(word) >= n:
                palindromes.add(word)
    return palindromes