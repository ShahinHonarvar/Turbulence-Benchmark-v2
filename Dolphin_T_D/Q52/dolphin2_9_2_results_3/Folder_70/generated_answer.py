def palindrome_of_length_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s) - 400):
        substr = s[i:i + 401]
        if substr == substr[::-1] and substr.isalpha():
            set_of_palindromes.add(substr)
    return set_of_palindromes