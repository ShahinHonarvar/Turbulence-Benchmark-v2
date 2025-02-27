from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()

    def find_palindromes(start, end):
        if end - start + 1 < 4:
            return set()
        chars = defaultdict(int)
        for i in range(start, end + 1):
            chars[s[i]] += 1
        palindromes = set()
        for i in range(start, end + 1):
            chars[s[i]] -= 1
            if is_palindrome(s[start:end + 1 - i] + s[i:end + 1]):
                palindromes.add(s[start:end + 1 - i] + s[i:end + 1])
            chars[s[i]] += 1
        return palindromes
    return find_palindromes(0, 4)