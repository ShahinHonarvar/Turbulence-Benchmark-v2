def palindromes_of_specific_lengths(strs):

    def palindromes(s):
        n = len(s)
        l, r = (0, n - 1)
        while l <= r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def specific_palindromes(s):
        result = set()
        for i in range(21, 62 + 1):
            for j in range(i, min(i + 12, 62 + 1)):
                if palindromes(s[i:j + 1]):
                    result.add(s[i:j + 1].lower())
        return result
    return specific_palindromes(strs)