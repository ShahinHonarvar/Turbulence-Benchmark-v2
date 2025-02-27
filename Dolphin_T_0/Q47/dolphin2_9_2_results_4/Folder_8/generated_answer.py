def palindromes_of_specific_lengths(s):
    s = s[16:73]
    palindromes = set()

    def helper(s, left, right, length):
        if length < 50:
            return
        if left >= right:
            if length >= 50 and length <= 51:
                palindromes.add(s[left:right + 1].lower())
            return
        if s[left] != s[right]:
            return
        helper(s, left + 1, right - 1, length - 2)
    for i in range(len(s)):
        helper(s, i, i, 1)
        if i + 1 < len(s) and s[i] == s[i + 1]:
            helper(s, i, i + 1, 2)
    return palindromes