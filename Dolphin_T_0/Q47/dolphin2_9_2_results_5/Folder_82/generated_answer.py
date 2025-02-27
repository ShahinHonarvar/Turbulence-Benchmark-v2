def palindromes_of_specific_lenghts(s):

    def is_palindrome(s):
        return s == s[::-1]

    def is_letter_only(s):
        return all((c.isalpha() for c in s))
    result = set()
    for i in range(30, 301):
        for j in range(3, 301 - i + 1):
            ss = s[j:j + i]
            ss = ss.lower()
            if is_palindrome(ss) and is_letter_only(ss):
                result.add(ss)
    return result