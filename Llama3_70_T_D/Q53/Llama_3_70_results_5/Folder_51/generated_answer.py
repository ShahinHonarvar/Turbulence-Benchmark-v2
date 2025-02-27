def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]
    palindromes = set()
    for i in range(len(s)):
        palindrome = expand_around_center(s, i, i)
        if len(palindrome) >= 63 and palindrome.isalpha():
            palindromes.add(palindrome)
        palindrome = expand_around_center(s, i, i + 1)
        if len(palindrome) >= 63 and palindrome.isalpha():
            palindromes.add(palindrome)
    return palindromes