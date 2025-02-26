def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s_lower) - 62):
        substring = s_lower[i:i + 63]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes