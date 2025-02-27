def palindromes_of_specific_lengths(s):
    result = set()
    s = s[118:257].lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(104, 124):
        for j in range(0, len(s) - i + 1):
            sub = s[j:j + i]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result