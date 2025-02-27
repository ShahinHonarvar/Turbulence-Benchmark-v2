def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    ans = set()
    for length in range(26, 32):
        target = s[33:86]
        for i in range(len(target) - length + 1):
            chunk = target[i:i + length]
            if all((c.isalpha() or not c.isalpha() for c in chunk.lower())):
                ans.add(chunk)
    return ans