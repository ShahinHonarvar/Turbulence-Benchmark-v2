def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - 89):
        substring = s_lower[i:i + 90]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes