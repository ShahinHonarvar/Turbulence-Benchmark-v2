def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    for i in range(1, 8):
        for j in range(i + 2, min(i + 5, 8)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result