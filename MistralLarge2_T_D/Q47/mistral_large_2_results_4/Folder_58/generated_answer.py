def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    sub_str = s[125:284]
    for length in range(109, 127):
        for i in range(len(sub_str) - length + 1):
            sub = sub_str[i:i + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub.lower())
    return palindromes