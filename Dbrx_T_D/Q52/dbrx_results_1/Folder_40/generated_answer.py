def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            if s[i] == s[j + 1] and s[i:j + 2] == s[i:j + 2][::-1]:
                palindromes.add(s[i:j + 2])
    return palindromes