def palindrome_of_length_at_least_n(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s)):
        for j in range(max(0, i - 79), i + 1):
            substring = s[i - j:i + 1]
            if substring.lower().isalpha() and (all((letter in english_letters for letter in substring.lower())) and len(substring) >= 81 and (substring == substring[::-1])):
                palindromes.add(substring)
    return palindromes