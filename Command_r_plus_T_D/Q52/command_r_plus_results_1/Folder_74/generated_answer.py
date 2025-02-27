def palindrome_of_length_n(s: str) -> set:
    length = len(s)
    palindromes = set()
    for i in range(length - 95):
        substring = s[i:i + 96]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes