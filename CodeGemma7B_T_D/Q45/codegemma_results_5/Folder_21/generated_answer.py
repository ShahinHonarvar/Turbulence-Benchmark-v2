def palindromes_between_indices(s):
    palindromes = set()
    for i in range(1, 9):
        for j in range(i, 9):
            substring = s[i:j + 1]
            lower = substring.lower()
            upper = lower[::-1]
            if lower == upper and len(substring) >= 7:
                palindromes.add(substring.capitalize())
    return palindromes