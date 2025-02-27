def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[200:301]
    length = len(substring)

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + 10, min(i + 51, length + 1)):
            cand = substring[i:j]
            if cand.isalpha() and is_palindrome(cand):
                result.add(cand)
    return result