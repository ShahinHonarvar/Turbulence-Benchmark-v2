def palindromes_of_specific_lengths(s):
    sub_string = s[125:284]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(109, 127):
        for j in range(0, len(sub_string) - i + 1):
            sub = sub_string[j:j + i]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes