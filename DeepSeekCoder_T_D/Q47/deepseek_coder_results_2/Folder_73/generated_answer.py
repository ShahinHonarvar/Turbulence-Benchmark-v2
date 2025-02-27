def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    lower_s = s.lower()
    for i in range(21, 63):
        for j in range(i + 22, min(i + 34, 63)):
            sub = lower_s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result