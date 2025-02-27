def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for i in range(100, 201):
        for j in range(i + 4, min(i + 11, 201)):
            sub = s[i:j + 1]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result