def palindromes_between_indices(s):
    valid_chars = [char for char in s[4:10] if char.isalpha() and char.isascii()]
    palindromes = set()
    n = len(valid_chars)
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes