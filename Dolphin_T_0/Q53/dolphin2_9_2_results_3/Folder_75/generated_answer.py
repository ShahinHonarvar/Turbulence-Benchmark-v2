def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 39, len(s)):
            sub = s[i:j + 1]
            if all((letter.isalpha() for letter in sub)) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes