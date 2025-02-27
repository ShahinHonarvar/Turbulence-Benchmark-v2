def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 8):
        for j in range(i, len(s) - i):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 9}