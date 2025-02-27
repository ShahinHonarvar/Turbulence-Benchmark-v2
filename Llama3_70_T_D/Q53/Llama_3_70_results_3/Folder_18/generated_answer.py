def palindrome_of_length_at_least_n(s):

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        return s[left + 1:right]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        palindrome_odd = expand_around_center(s, i, i)
        if len(palindrome_odd) >= 62 and palindrome_odd.isalpha():
            palindromes.add(palindrome_odd)
        palindrome_even = expand_around_center(s, i, i + 1)
        if len(palindrome_even) >= 62 and palindrome_even.isalpha():
            palindromes.add(palindrome_even)
    return palindromes