def palindrome_of_length_at_least_n(s):
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if len(s[i:j]) >= 57 and s[i:j].lower() == s[i:j][::-1].lower() and s[i:j].isalpha():
                set_of_palindromes.add(s[i:j])
    return set_of_palindromes