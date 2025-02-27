def palindrome_of_length_n(s):
    return set((p for p in get_palindromes(s.lower()) if len(p) == n))

def get_palindromes(s):
    palindromes = set()
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                palindromes.add(s[i:j + 1])
    return palindromes