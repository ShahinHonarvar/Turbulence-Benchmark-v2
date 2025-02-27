def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    substring = s[2:9].lower()
    letters = [char for char in substring if char.isalpha()]
    for i in range(7, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            window = letters[j:j + i]
            if window == window[::-1]:
                palindromes.add(''.join(window))
    return palindromes