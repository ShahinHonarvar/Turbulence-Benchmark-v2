def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 55):
        for j in range(i + 28, len(s) - i):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes