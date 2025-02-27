def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 94 + 1):
        for j in range(94):
            if s[i:i + j + 1] == s[i:i + j + 1][::-1] and s[i:i + j + 1].isalpha():
                palindromes.add(s[i:i + j + 1])
    return {p for p in palindromes if len(p) >= 94}