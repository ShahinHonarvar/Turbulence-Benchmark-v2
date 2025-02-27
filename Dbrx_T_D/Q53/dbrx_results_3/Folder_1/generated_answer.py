def palindrome_of_length_at_least_n(s):
    english_letters = set(english_lowercase_letters + english_uppercase_letters)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 28):
        for j in range(i + 14, len(s) - i):
            if s[i:j + 1] == s[i:j + 1][::-1] and all((c in english_letters for c in s[i:j + 1])):
                palindromes.add(s[i:j + 1])
    return palindromes