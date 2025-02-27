def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for i in range(11):
        for j in range(i + 3, min(i + 6, 11)):
            sub = s[i:j].lower()
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result