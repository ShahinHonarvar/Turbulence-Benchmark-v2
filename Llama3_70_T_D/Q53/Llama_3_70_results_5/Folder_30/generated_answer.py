def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]
    palindromes = set()
    for i in range(len(s)):
        palindrome1 = expand_around_center(s, i, i)
        palindrome2 = expand_around_center(s, i, i + 1)
        if len(palindrome1) >= 16 and palindrome1.isalpha():
            palindromes.add(palindrome1)
        if len(palindrome2) >= 16 and palindrome2.isalpha():
            palindromes.add(palindrome2)
    return palindromes