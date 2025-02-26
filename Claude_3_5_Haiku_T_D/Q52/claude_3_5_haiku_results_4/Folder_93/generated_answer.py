def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for start in range(length - 44):
        for end in range(start + 45, length + 1):
            substring = string[start:end]
            if len(substring) == 45:
                substring_lower = substring.lower()
                if substring_lower == substring_lower[::-1] and substring_lower.isalpha():
                    palindromes.add(substring)
    return palindromes