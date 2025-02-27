def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    sub_str = s[124:284].lower()
    for length in range(115, 135):
        for i in range(124, 284 - length + 1):
            sub = sub_str[i - 124:i - 124 + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes