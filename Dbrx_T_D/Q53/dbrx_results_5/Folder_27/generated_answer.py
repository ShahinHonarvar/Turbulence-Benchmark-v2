def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 100 + 1):
        for j in range(100):
            if s[i:i + j + 1] == s[i:i + j + 1][::-1] and s[i:i + j + 1].isalpha():
                palindromes.add(s[i:i + j + 1])
    return {palindrome for palindrome in palindromes if len(palindrome) >= 100}