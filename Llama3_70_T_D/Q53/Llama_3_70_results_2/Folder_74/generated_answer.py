def palindrome_of_length_at_least_n(s):

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
            left -= 1
            right += 1
        return s[left + 1:right]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        palindrome = expand_around_center(s, i, i)
        if len(palindrome) >= 57:
            palindromes.add(palindrome)
        palindrome = expand_around_center(s, i, i + 1)
        if len(palindrome) >= 57:
            palindromes.add(palindrome)
    return set((palindrome for palindrome in palindromes if palindrome.isalpha()))